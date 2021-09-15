from client.models import policy_holder
from policyBaazar.models import UserProfile,User
from django.shortcuts import redirect, render
from agent.models import Insurance_Policy,Main_Category,Main_SubCategory
from django.contrib.auth.decorators import login_required
from .models import policy_holder,home_details, vehicle_details,mobile_details,health_details,travel_details,life_details
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    mobj = Main_Category.objects.all()
    return render(request,"welcomeclient.html", {'mobj':mobj})

def house(request):
    return render(request, "house.html")

# def house_insurance(request):
#     iobj = Insurance_Policy.objects.all()

#     return render(request, "home_insurance.html", {'iobj':iobj})

# def vehicle_insurance(request):
#     return render(request, "vehicle_insurance.html")

# def travel_insurance(request):
#     return render(request, "travel_insurance.html")

# def health_insurance(request):
#     return render(request, "health_insurance.html")

# def life_insurance(request):
#     return render(request, "life_insurance.html")

# def mobile_insurance(request):
#     return render(request, "mobile_insurance.html")

def pages(request, id):
     if id == 1:
         iobj = Insurance_Policy.objects.filter(catid=id)

         return render(request,"home_insurance.html",{'iobj':iobj})
     elif id == 2:
         iobj = Insurance_Policy.objects.filter(catid =id)

         return render(request,"vehicle_insurance.html",{'iobj':iobj})
     elif id == 3:
         iobj = Insurance_Policy.objects.filter(catid = id)

         return render(request,"travel_insurance.html",{'iobj':iobj})
     elif id == 4:

         iobj = Insurance_Policy.objects.filter(catid = id)

         return render(request,"health_insurance.html",{'iobj':iobj})
     elif id == 5:

         iobj = Insurance_Policy.objects.filter(catid = id)

         return render(request,"life_insurance.html",{'iobj':iobj})
     elif id == 6:

         iobj = Insurance_Policy.objects.filter(catid = id)

         return render(request,"mobile_insurance.html",{'iobj':iobj})
        #sobj = Main_SubCategory.objects.filter(catid = id)

    # return render(request, "pages.html")
def home_form(request,id):
    try:
        if request.method == "POST":
            addr1 = request.POST['addr1']
            addr2 = request.POST['addr2']
            city = request.POST['city']
            pincode = request.POST['Pincode']
            area = request.POST['area']
            uobj = UserProfile.objects.get(user__username=request.user)

            hobj = home_details(add_line1=addr1, add_line2=addr2, city=city, pincode=pincode, area=area, user_id=uobj)
            hobj.save()
            pid = Insurance_Policy.objects.get(id=id)
            uid = UserProfile.objects.get(user__username=request.user)
            pobj = policy_holder(placedby=uid, policy_id=pid)
            pobj.save()
            return redirect('/client/order/')
    except:
        messages.error(request,"policy already taken by u.")
        return redirect('/client/order/')
     
    return render(request,"home_form.html")

def vehicle_form(request,id):
    try:
        if request.method == "POST":
            regs = request.POST['regs']
            chas = request.POST['chas']
            model = request.POST['model']
            color = request.POST['color']
            year = request.POST['year']
            uobj = UserProfile.objects.get(user__username=request.user)

            vobj = vehicle_details(registration_no=regs, chassis_no=chas, model=model, color=color, year=year, user_id=uobj)
            vobj.save()
            pid = Insurance_Policy.objects.get(id=id)
            uid = UserProfile.objects.get(user__username=request.user)
            pobj = policy_holder(placedby=uid, policy_id=pid)
            pobj.save()
            return redirect('/client/order')
    except:
        return redirect('/client/prblm/')


    return render(request,"vehicle_form.html")

def travel_form(request,id):
    try:
        if request.method == "POST":
            travel = request.POST['travel']
            start = request.POST['start']
            end = request.POST['end']
            passengers = request.POST['nmbr']
            uobj = UserProfile.objects.get(user__username=request.user)

            tobj = travel_details(travelling_to=travel, start_Date=start, End_Date=end, passengers=passengers, user_id=uobj)
            tobj.save()
            pid = Insurance_Policy.objects.get(id=id)
            uid = UserProfile.objects.get(user__username=request.user)
            pobj = policy_holder(placedby=uid, policy_id=pid)
            pobj.save()
            return redirect('/client/order')

    except:
        return redirect('/client/prblm/')


    return render(request,"travel_form.html")

def health_form(request,id):
    try:
        if request.method == "POST":
            name = request.POST['name']
            dob = request.POST['dob']
            current_doctor = request.POST['cd']
            date_visit = request.POST['ld']
            occupation = request.POST['occupation']
            uobj = UserProfile.objects.get(user__username=request.user)

            hobj = health_details(name=name, dob=dob, current_doctor=current_doctor, date_visit=date_visit, occupation=occupation, user_id=uobj)
            hobj.save()
            pid = Insurance_Policy.objects.get(id=id)
            uid = UserProfile.objects.get(user__username=request.user)
            pobj = policy_holder(placedby=uid, policy_id=pid)
            pobj.save()
            return redirect('/client/order') 
    except:
        return redirect('/client/prblm/')
    


    return render(request,"health_form.html")

def life_form(request, id):
   
    try:
        if request.method == "POST":
            name = request.POST['name']
            dob = request.POST['dob']
            height = request.POST['height']
            weight = request.POST['weight']
            health_issue = request.POST['health']
            uobj = UserProfile.objects.get(user__username=request.user)

            lobj = life_details(name=name, dob=dob, height=height, weight=weight, health_issue=health_issue, user_id=uobj)
            lobj.save()
            pid = Insurance_Policy.objects.get(id=id)
            uid = UserProfile.objects.get(user__username=request.user)
            pobj = policy_holder(placedby=uid, policy_id=pid)
            pobj.save()
            return redirect('/client/order')
    except:
        return redirect('/client/prblm/')
    return render(request,"life_form.html")

def mobile_form(request, id):
    try:
        if request.method == "POST":
            company = request.POST['name']
            model = request.POST['model']
            color = request.POST['color']
            year = request.POST['year']
            uobj = UserProfile.objects.get(user__username=request.user)

            mobj = mobile_details(company_name=company, model=model, color=color, purchasing_date=year, user_id=uobj)
            mobj.save()
            pid = Insurance_Policy.objects.get(id=id)
            uid = UserProfile.objects.get(user__username=request.user)
            pobj = policy_holder(placedby=uid, policy_id=pid)
            pobj.save()
            return redirect('/client/order')
    except:
        return redirect('/client/prblm/')
    return render(request,"mobile_form.html")

def history(request):
    uobj = UserProfile.objects.get(user__username=request.user)
    pobj = policy_holder.objects.filter(placedby=uobj.id)
    return render(request,"history.html", {'pobj':pobj})

def order(request):
    return render(request,"order.html")

def prblm(request):
    return render(request, "error.html")

def myaccount(request):
    uobj = UserProfile.objects.filter(user__username=request.user)
    

    return render(request, "myaccount.html", {'uobj':uobj})