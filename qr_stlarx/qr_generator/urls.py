from django.urls import path

from . import views

urlpatterns = [
    path('str2qr', views.qr_strgen, name='str2qr'),
    path('pdf2qr', views.mon_index, name='pdf2qr'),
]
