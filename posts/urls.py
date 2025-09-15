from django.urls import path
from .views import *

urlpatterns = [
    path('cbv-lista/', PostListView.as_view(), name='cbv_lista_posts'),
    path('novo/', PostCreateView.as_view(), name='novo_post'),
    path('lista/', PostListView.as_view(), name='lista_posts'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
    path('<int:pk>/detalhes/', view=detalhes_post, name='detalhes_post')
]
#Rian Prates