from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.criar_vilao, name='criar_vilao'),
    path('', views.lista_viloes, name='lista_viloes'),
    path('<int:pk>/', views.detalhe_vilao, name='detalhe_vilao'),
    path('<int:pk>/editar/', views.editar_vilao, name='editar_vilao'),
    path('<int:pk>/excluir/', views.excluir_vilao, name='excluir_vilao'),
]

# Rian Prates