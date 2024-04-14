
from django.contrib import admin
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('',mode1,name="home"),
    path('home',mode1,name="home"),
    path('about/',mode2,name="about"),
    path('service/',mode3,name="service"),
    path('team/',mode4,name="team"),
    path('why/',mode5,name="why"),
    path('admin/', admin.site.urls),
]
