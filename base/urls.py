# base/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sheet/', views.UploadFile.as_view(), name='upload_excel_sheet'),
]
