"""BeautyParlourManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beauty.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('about',About,name="about"),
	path('gallery',gallery,name="gallery"),
    path('contact',Contact,name="contact"),
    path('login',Login,name="login"),
    path('logout',Logout,name="logout"),
    path('login_admin',Admin_Login,name="login_admin"),
    path('signup',Signup,name="signup"),
    path('profile',Profile,name="profile"),
    path('edit_profile',Edit_Profile,name="edit_profile"),
    path('admin_home',Admin_Home,name="admin_home"),
    path('view_user',View_user,name="view_user"),
    path('view_service',View_Service,name="view_service"),
    path('all_service',All_Service,name="all_service"),
	path('all_service1',All_Service1,name="all_service1"),
    path('add_service',Add_Service,name="add_service"),
    path('book_appointment',Book_Appointment,name="book_appointment"),
    path('book_select_appointment(<int:pid>)',Book_Selected_Appointment,name="book_select_appointment"),
    path('view_new_user',View_New_user,name="view_new_user"),
    path('view_new_appointment',View_New_Appointment,name="view_new_appointment"),
    path('all_appointment',All_Appointment,name="all_appointment"),
    path('view_appointment',View_Appointment,name="view_appointment"),
    path('confirm_appointment',View_Confirm_Appointment,name="confirm_appointment"),
    path('change_password',Change_Password,name="change_password"),
    path('assign_user_status(<int:pid>)',Assign_user_status,name="assign_user_status"),
    path('assign_book_status(<int:pid>)',Assign_book_status,name="assign_book_status"),
    path('delete_appointment(<int:pid>)',delete_appointment,name="delete_appointment"),
    path('delete_service(<int:pid>)',delete_service,name="delete_service"),
    path('delete_user(<int:pid>)',delete_user,name="delete_user"),
    path('payment(<int:pid>)',payment,name="payment"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
