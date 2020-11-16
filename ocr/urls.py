from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'ocr'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image', csrf_exempt(views.upload_image), name='upload_image'),
    path('get_crop_and_ocr', csrf_exempt(views.get_crop_and_ocr), name='get_crop_and_ocr'),
]