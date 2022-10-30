
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name="about-us"),
    path('our-services/', views.our_services, name="our-services"),
    path('contact-us/', views.contact_us, name="contact-us"),
]
