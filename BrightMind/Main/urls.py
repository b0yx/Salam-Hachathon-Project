from django.urls import path
from . import views

urlpatterns = [
    path('api/Test1/', views.Test1.as_view(), name='Test1'),
    path('api/Test2/', views.Test2.as_view(), name='Test2'),
]