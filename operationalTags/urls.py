from django.urls import path

from operationalTags.views import *


app_name="JOPT"

urlpatterns = [
    path("joper/",joper,name='joper'),
    path("oper/",oper,name="oper"),
]
