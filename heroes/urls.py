from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.criar_heroi, name='criar_heroi'),
    path('', views.lista_herois, name='lista_herois'),
    path('<int:pk>/', views.detalhe_heroi, name='detalhe_heroi'),
    path('<int:pk>/editar/', views.editar_heroi, name='editar_heroi'),
    path('<int:pk>/excluir/', views.excluir_heroi, name='excluir_heroi'),
]
# Rian Prates