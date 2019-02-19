from django.urls import path

from . import views

app_name = 'fileupload'

urlpatterns = [
    path('', views.upload, name='upload'),
    path('extraction/action/', views.codeprocess, name='codeprocess'),
    path('extraction/<str:code>/', views.extraction, name='extraction'),
]
