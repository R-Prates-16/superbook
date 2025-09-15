from django.urls import path
from .views import *

urlpatterns = [
    path('novo/', PostCreateView.as_view(), name='novo_comment'),
]