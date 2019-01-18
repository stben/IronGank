"""upload urls"""
from django.urls import path
from upload.views import upload_file

urlpatterns = [
    path('', upload_file),
]
