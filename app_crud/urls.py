from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('novo/', views.criar_equipamento, name='criar_equipamento'),
    path('<int:pk>/editar/', views.atualizar_equipamento, name='atualizar_equipamento'),
    path('<int:pk>/excluir/', views.excluir_equipamento, name='excluir_equipamento'),
]
