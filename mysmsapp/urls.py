from django.urls import path
from . import views

app_name='mysmsapp'

urlpatterns = [

path('',views.homepage,name="index"),

path('send',views.broadcast_sms,name="blast_broadcast"),

]