from django.urls import path
from printingTags.views import *
app_name="JPT"
urlpatterns = [
    path("printNames/",printNames,name='printNames'),
]
