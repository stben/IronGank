from django.urls import path
from upload.views import *

urlpatterns = [
    path('', upload_file),
]
