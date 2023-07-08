from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Proveedor, Plato, Cliente, Pedido, Repartidor, RutaEntrega, CategoriaPlato, Ingrediente
from .forms import ClienteForm, PedidoForm, LoginForm

def index(request):
    user = request.user
    first_name = user.first_name if user.is_authenticated else None
    last_name = user.last_name if user.is_authenticated else None
    context = {
        'first_name': first_name,
        'last_name': last_name
    }
    return render(request, 'index.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'nosotros.html')

def staff(request):
    return render(request, 'equipo.html')

def contact(request):
    return render(request, 'contacto.html')


# Vista de catálogo de platos
def catalogo_platos(request):
    categorias = CategoriaPlato.objects.all()
    ingredientes = Ingrediente.objects.all()
    platos = Plato.objects.all()
    context = {
        'categorias': categorias,
        'ingredientes': ingredientes,
        'platos': platos
    }
    return render(request, 'catalogo_platos.html', context)

# Vista de detalle de plato
def detalle_plato(request, plato_id):
    plato = Plato.objects.get(id=plato_id)
    context = {
        'plato': plato
    }
    return render(request, 'detalle_plato.html', context)

# Vista de registro de cliente
def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        user = User.objects.create_user(username=nombre, password='contrasena')
        cliente = Cliente(nombre=nombre, direccion=direccion)
        cliente.save()
        return redirect('inicio')
    return render(request, 'registro_cliente.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # El usuario no existe
                user = None

            if user is not None and user.check_password(password):
                # La contraseña es válida
                login(request, user)
                return redirect('index')
    # Redirige a la página de inicio en caso de fallo de inicio de sesión
    return redirect('index')
    

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

# Vista de crear pedido
def crear_pedido(request):
    platos = Plato.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        platos_ids = request.POST.getlist('platos')
        fecha_entrega = request.POST['fecha_entrega']
        hora_entrega = request.POST['hora_entrega']
        es_entrega_domicilio = 'es_entrega_domicilio' in request.POST

        cliente = Cliente.objects.get(id=cliente_id)
        platos = Plato.objects.filter(id__in=platos_ids)
        precio_total = sum(plato.precio for plato in platos)

        pedido = Pedido(cliente=cliente, fecha_entrega=fecha_entrega, hora_entrega=hora_entrega, es_entrega_domicilio=es_entrega_domicilio)
        pedido.save()
        pedido.platos.set(platos)
        return redirect('estado_pedido', pedido_id=pedido.id)

    context = {
        'platos': platos
    }
    return render(request, 'crear_pedido.html', context)

# Vista de estado de pedido
def estado_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    context = {
        'pedido': pedido
    }
    return render(request, 'estado_pedido.html', context)

# Vista de configuración de cuenta
def configuracion_cuenta(request):
    # Lógica para configurar la cuenta
    return render(request, 'cuenta.html')

# Vista de tablero de indicadores
def tablero_indicadores(request):
    cantidad_pedidos = Pedido.objects.count()
    monto_promedio_venta = Pedido.objects.aggregate(models.Avg('precio_total'))

    context = {
        'cantidad_pedidos': cantidad_pedidos,
        'monto_promedio_venta': monto_promedio_venta,
    }
    return render(request, 'tablero.html', context)

# Resto de vistas para completar

# ...

# Vista de gestión de usuarios
def gestion_usuarios(request):
    # Lógica para gestionar usuarios
    return render(request, 'gestion_usuarios.html')

# Vista de gestión de proveedores
def gestion_proveedores(request):
    # Lógica para gestionar proveedores
    return render(request, 'gestion_proveedores.html')

# Vista de gestión de repartidores
def gestion_repartidores(request):
    # Lógica para gestionar repartidores
    return render(request, 'gestion_repartidores.html')

# Vista de creación de ruta de entrega
def crear_ruta_entrega(request):
    # Lógica para crear ruta de entrega
    return render(request, 'crear_ruta_entrega.html')

# Vista de detalle de ruta de entrega
def detalle_ruta_entrega(request, ruta_id):
    ruta_entrega = RutaEntrega.objects.get(id=ruta_id)
    context = {
        'ruta_entrega': ruta_entrega
    }
    return render(request, 'detalle_ruta_entrega.html', context)

# Vista de historial de rutas de entrega
def historial_rutas_entrega(request):
    rutas_entrega = RutaEntrega.objects.all()
    context = {
        'rutas_entrega': rutas_entrega
    }
    return render(request, 'historial_rutas_entrega.html', context)

# Resto de vistas para completar

# ...

