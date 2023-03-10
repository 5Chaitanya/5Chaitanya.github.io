from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from gsignup.views import gsignaction
from glogin.views import gloginaction
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
    path('gsignup/',gsignaction),
    path('glogin',gloginaction),
]
