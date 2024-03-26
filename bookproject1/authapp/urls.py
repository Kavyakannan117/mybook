from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.userRegistration,name='register'),
    path('',views.Login,name="login"),
    path('adminview/',views.admin_view,name="admin_view"),
    path('userlogin/',views.user_view,name='user_view'),
    path('logout/',views.log_out,name='logout'),

]
