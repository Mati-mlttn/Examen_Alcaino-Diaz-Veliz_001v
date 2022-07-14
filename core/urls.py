from django.urls import path, include
from .views import home,productos,quienes,contacto,adopcion,login,agregar_producto,listar_productos,modificar_producto, eliminar_producto,productoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', productoViewset)

urlpatterns = [
    path('',home, name="home"),
    path('productos/',productos, name="productos"),
    path('quienes/',quienes, name="quienes"),
    path('contacto/',contacto, name="contacto"),
    path('adopcion/',adopcion, name="adopcion"),
    path('login/',login, name="login"),
    path('agregar-producto/',agregar_producto, name="agregar_producto"),
    path('listar-productos/',listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/',modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto, name="eliminar_producto"),
    path('api/', include(router.urls) ),
]
