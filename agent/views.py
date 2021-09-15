from django.shortcuts import redirect, render
from .models import Main_Category, Main_SubCategory, Insurance_Policy
from policyBaazar.models import User, UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from client.models import policy_holder


# Create your views here.
@login_required
def home(request):
    uobj = UserProfile.objects.filter(usertype="client")
    ubj = len(uobj)

    polcobj = Insurance_Policy.objects.all()
    plcobj = len(polcobj)

    catobj = Main_Category.objects.all()
    cobj = len(catobj)

    sobjs = Main_SubCategory.objects.all()
    sobj = len(sobjs)

    pobj = policy_holder.objects.all()
    pobjs = len(pobj)

    return render(request,"welcomeagent.html",{'ubj':ubj, 'plcobj':plcobj, 'cobj':cobj, 'sobj':sobj, 'pobjs':pobjs})

@login_required
def category(request):
    if request.method == 'POST':
        catname = request.POST['catname']
        catdesc = request.POST['catdesc']
        cat_image = request.FILES['image']
        try:
            cobj = Main_Category(catname=catname, catdesc=catdesc, cat_image=cat_image)
            cobj.save()
            return redirect('/agent/category/')
        except:
            return render(request,  "prblm.html")

    return render(request,"category.html")

@login_required
def manage_category(request):
    cobj = Main_Category.objects.all()
    return render(request,"manage_category.html", {'cobj':cobj})

@login_required
def Add_SubCategory(request):
    cobj = Main_Category.objects.all()
    
    if request.method == 'POST':
        catname = request.POST['catname']
        catid = request.POST['cat']
        cid = Main_Category.objects.get(id=catid)
        try:

            aobj = Main_SubCategory(sub_catname=catname, catid=cid)
            aobj.save()
        except:
            return render(request,  "prblm.html")

    return render(request, "Add_SubCategory.html",{'cobj':cobj})

@login_required
def Manage_SubCategory(request):
    catname = Main_SubCategory.objects.all()

    return render(request, "Manage_SubCategory.html", {'catname':catname})


@login_required
def add_policy(request):
    cobj = Main_Category.objects.all()
    sobj = Main_SubCategory.objects.all()

    if request.method == "POST":
        cname = request.POST['cname']
        sbc = request.POST['sbc']
        pname = request.POST['pname']
        sub = request.POST['sub']
        premium = request.POST['premium']
        tenure = request.POST['tenure']
       # cbobj = Category(catname=pass)
        cbj = Main_Category.objects.get(id=cname)
        sbj = Main_SubCategory.objects.get(id=sbc)
        try:
            pobj = Insurance_Policy(policy_name=pname, sum_assured=sub, premium=premium, tenure=tenure, catid=cbj, sub_id=sbj)
            pobj.save()
            #messages.SUCCESS(request,  "policy added successfully...")
            return redirect('/agent/add_policy/')
        except:
            return render(request,  "prblm.html")
            #return redirect('/agent/home/')
    return render(request,"add_policy.html", {'cobj':cobj, 'sobj':sobj})

@login_required
def manage_policy(request):
    iobj = Insurance_Policy.objects.all()

    return render(request,"manage_policy.html", {'iobj':iobj})

@login_required
def update_category(request,id):
    if request.method== "POST":
        catname = request.POST['catname']
        catobj = Main_Category.objects.filter(id=id)
        catobj.update(catname=catname)
        return redirect('/agent/manage_category/')
    return render(request,"updcat.html")
    


@login_required
def delete_category(request, id):
    catobj = Main_Category.objects.get(id=id)
    catobj.delete()
    #delete from main_category where id = id
    return redirect('/agent/manage_category/')

@login_required
def update_sub(request, id):

    if request.method=="POST":
        subcatname = request.POST['subcatname']
        subobj = Main_SubCategory.objects.filter(id=id)
        subobj.update(sub_catname=subcatname)
        return redirect('/agent/Manage_SubCategory/')

    return render(request, "updsub.html")

@login_required
def delete_sub(request, id):
    subobj = Main_SubCategory.objects.get(id=id)
    subobj.delete()
    return redirect('/agent/Manage_SubCategory/')

@login_required
def update_policy(request, id):
    cobj = Main_Category.objects.all()
    sobj = Main_SubCategory.objects.all()

    if request.method == "POST":
        sbc = request.POST['sbc']
        pname = request.POST['pname']
        sub = request.POST['sub']
        premium = request.POST['premium']
        tenure = request.POST['tenure']

        iobj = Insurance_Policy.objects.filter(id=id)
        iobj.update(sub_id=sbc, policy_name=pname, tenure=tenure, premium=premium, sum_assured=sub)

        return redirect('/agent/manage_policy/')
        
    return render(request, "updatepolicy.html", {'cobj':cobj, 'sobj':sobj})

@login_required
def delete_policy(request,id):
    iobj = Insurance_Policy.objects.get(id=id)
    iobj.delete()
    return redirect('/agent/manage_policy/')

@login_required
def delete_user(request,id):
    uobj = UserProfile.objects.get(id=id)
    uobj.delete()
    return redirect('/agent/user/')

@login_required
def delete_policy_holder(request,id):
    pobj = policy_holder.objects.get(id=id)
    pobj.delete()
    return redirect('/agent/policy_holder/')

def user(request):
    uobj = UserProfile.objects.all()
    return render(request,"user.html",{'uobj':uobj})

def policyholder(request):
    pobj = policy_holder.objects.all()
    
    return render(request,"policyholder.html",{'pobj':pobj})

