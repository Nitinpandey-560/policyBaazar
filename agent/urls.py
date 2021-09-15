from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home),
    path('category/', views.category),
    path('manage_category/', views.manage_category),
    path('Add_SubCategory/', views.Add_SubCategory),
    path('Manage_SubCategory/', views.Manage_SubCategory),
    path('add_policy/', views.add_policy),
    path('manage_policy/', views.manage_policy),
    path('update/<int:id>/', views.update_category, name="upd_category"),
    path('delete/<int:id>/', views.delete_category, name="del_category"),
    path('updatesub/<int:id>/', views.update_sub, name="update_sub"),
    path('deletesub/<int:id>/', views.delete_sub, name="delete_sub"),
    path('updatepolicy/<int:id>/', views.update_policy, name="upd_policy"),
    path('deletepolicy/<int:id>/', views.delete_policy, name="del_policy"),
    path('deleteuser/<int:id>/', views.delete_user, name="del_user"),
    path('deletepolicy/<int:id>/', views.delete_policy_holder, name="del_policy_holder"),
    path('user/', views.user),
    path('policyholder/', views.policyholder)

]