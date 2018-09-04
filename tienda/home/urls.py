from django.urls import path
from .views import *

urlpatterns = [ 
path('', vista_about),
path('contacto/', vista_contacto),
path('lista_producto/', vista_lista_producto, name='vista_lista_producto'),
path('listar_marca/',vista_listar_marca, name='vista_listar_marca'),
path('listar_categoria/',vista_listar_categoria, name='vista_listar_categoria'),
path('agregar_producto/',vista_agregar_producto, name='vista_agregar_producto'),
path('agregar_marca/',vista_agregar_marca, name='vista_agregar_marca'),
path('agregar_categoria/',vista_agregar_categoria, name='vista_agregar_categoria'),
path('crear_perfil/', vista_crear_perfil, name='vista_crear_perfil'),
path('ver_marca/',vista_ver_marca, name='vista_ver_marca'),
path('editar_marca/',vista_editar_marca, name='vista_editar_marca'),
path('ver_categoria/',vista_ver_categoria, name='vista_ver_categoria'),
path('editar_categoria/',vista_editar_categoria, name='vista_editar_categoria'),
path('ver_producto/<int:id_prod>/', vista_ver_producto, name='vista_ver_producto'),
path('editar_producto/<int:id_prod>/', vista_editar_producto, name='vista_editar_producto'),
path('eliminar_marca/<int:id_prod>/', vista_eliminar_marca, name='vista_eliminar_marca'),
path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto, name='vista_eliminar_producto'),
path('eliminar_categoria/<int:id_prod>/', vista_eliminar_categoria, name='vista_eliminar_categoria'),
path('login/',vista_login, name='vista_login'),
path('logout/',vista_logout, name='vista_logout'),
path('register/',vista_register, name='vista_register'),




]