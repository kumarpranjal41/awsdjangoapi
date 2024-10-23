
from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework import routers
from pranjalmobile.views import signupviewset

router = routers.DefaultRouter()
router.register(r'signup' , signupviewset)



urlpatterns = [
    path('' , include(router.urls) )
   
   
]
