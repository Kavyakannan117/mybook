from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.RegisterUser,name='register'),
    path('',views.LoginUser,name="login"),
    path('adminview/',views.admin_view,name="admin_view"),
  
    path('logout/',views.log_out,name='logout'),

]
