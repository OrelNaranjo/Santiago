from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('menu/', views.catalogo_platos, name='menu'),
    path('nosotros/', views.about, name='about'),
    path('equipo/', views.staff, name='staff'),
    path('contacto/', views.contact, name='contact'),
    path('detalle/<int:plato_id>/', views.detalle_plato, name='detalle_plato'),
    path('registro/', views.registrar_cliente, name='registrar_cliente'),
    path('login/', views.login, name='login'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('nuevo-pedido/<int:pedido_id>/', views.crear_pedido, name='crear_pedido'),
    path('estado-pedido/<int:pedido_id>/', views.estado_pedido, name='estado_pedido'),
    path('cuenta/', views.configuracion_cuenta, name='configuracion_cuenta'),
    path('tablero/', views.tablero_indicadores, name='tablero_indicadores'),
    # Resto de rutas para completar
    # ...
    path('usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('proveedores/', views.gestion_proveedores, name='gestion_proveedores'),
    path('repartidores/', views.gestion_repartidores, name='gestion_repartidores'),
    path('ruta-entrega/', views.crear_ruta_entrega, name='crear_ruta_entrega'),
    path('detalle-ruta-entrega/<int:ruta_id>/', views.detalle_ruta_entrega, name='detalle_ruta_entrega'),
    path('historial-ruta/', views.historial_rutas_entrega, name='historial_rutas_entrega'),
    # Resto de rutas para completar
    # ...
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
