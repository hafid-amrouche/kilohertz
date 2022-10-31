
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name="about-us"),
    path('our-services/', views.our_services, name="our-services"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('messages/', views.messages, name="messages"),
)
