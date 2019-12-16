from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from app3 import views


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path("gk/",views.gop),
    path("vk/",views.vek),
    path("rk/",views.rk),
    path("mk/",views.mk),
    path("html/",views.template),
    path("myimg/",views.myimg),
    path("time/", views.time),
   
]