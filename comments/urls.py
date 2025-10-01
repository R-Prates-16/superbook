from django.urls import path
from .views import *

urlpatterns = [
    path('novo/<int:post_id>/', criar_comentario, name='novo_comment'),
    path('<int:pk>/editar/', EditarComentarioView.as_view(), name='editar_comment'),
    path('<int:pk>/excluir/', ExcluirComentarioView.as_view(), name='excluir_comment'),
]

# Rian Prates