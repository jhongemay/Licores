from django.shortcuts import render, redirect
from .forms import *
from .models import *		
# Create your views here.	
def vista_about(request):
	return render(request,'about.html')


def vista_contacto(request):
	info_enviado=False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		fomulario = contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text = formulario.cleaned_data['texto']
	else:
		formulario = contacto_form()
	return render(request,'contacto.html',locals()) 
	
def vista_lista_producto (request):
    lista = Producto.objects.all()
    return render(request, 'lista_producto.html', locals())
def vista_agregar_producto(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form()
	return render(request, 'agregar_producto.html', locals())


def vista_listar_marca (request):
	marca = Marca.object.all()
	return render(request, 'lista_marca.html', locals())


def vista_agregar_marca (request):
	if request.method == 'POST':
		formulario = agregar_marca_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/listar_marca/')
	else:
		formulario = listar_marca_form()
	return render(request, 'agregar_marca.html', locals())


def vista_listar_categoria (request):
	categoria = categoria.objects.all()
	return render(request, 'listar_categoria.html', locals())


def vista_agregar_categoria (request):
	if request.method == 'POST':
		formulario = agregar_categoria_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/listar_categoria/')
	else:
			formulario = agregar_categoria_form()
	return render(request, 'agregar_categoria.html', locals())


def vista_crear_perfil (request):
	perfil = perfil.objects.all()
	return render(request, 'crear_perfil.html', locals())

def vista_agregar_pefil (request):
	if request.method == 'POST':
		formulario = agregar_perfil_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
		return redirect ('/crear_perfil/')
	else:
		formulario = agregar_categoria_form()
	return render(request, 'agregar_perfil.html', locals())


def vista_ver_marca (request):
	marca = marca.objects.all()
	return render(request, 'ver_marca.html', locals())

def vista_editar_categoria (request):
	categoria = categoria.objects.all()
	return render(request, 'editar_categoria.html', locals())

def vista_editar_marca (request):
	marca = marca.objects.all()
	return render(request, 'editar_marca.html', locals())

def vista_ver_categoria (request):
	categoria = categoria.objects.all()
	return render(request, 'ver_categoria.html', locals())

def vista_editar_categoria (request):
	categoria = categoria.objects.all()
	return render(request, 'editar_categoria.html', locals())

def vista_eliminar_marca (request):
	marca = marca.objects.all()
	return render(request, 'eliminar_marca.html', locals())

def vista_eliminar_categoria (request):
	categoria = categoria.objects.all()
	return render(request, 'eliminar_categoria.html', locals())














def vista_ver_producto(request, id_prod):
		p = Producto.objects.get(id=id_prod)
		return render(request,'ver_producto.html',locals())

def vista_editar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	if request.method == "POST":
		formulario = agregar_producto_form(request.POST, request.FILES, instance=prod)
		if formulario.is_valid():
			prod = formulario.save()
			return redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form(instance = prod)
	return render(request, 'vista_agregar_producto.html', locals())

def vista_eliminar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	prod.delete()
	return redirect ('/lista_producto')

def vista_login (request):
	usu = ""
	cla = ""
	if request.method == "POST":
		fomulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if  usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	return render(request, 'login.html', locals())

def vista_logout (request):
	logout(request)
	return redirect('/login/')

def vista_register (request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo,password=password_1)
			u.save()
			return render(request, 'tanks_for_register.html', locals())
		else:
			return render(request, 'register.html', locals())
		return render(request, 'register.html', locals())



