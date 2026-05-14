from django.shortcuts import render, redirect 
from django.http import HttpResponse


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from .forms import clienteForm, UsuarioForm
from .models import cliente

# Create your views here.
@login_required
def novo_cliente(request):
    template_name = 'novo_cliente.html'
    clientes = cliente.objects.all()
    context = {} 
    if request.method == 'POST':
        form = clienteForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('novo_cliente') 
        else:
             print(form.errors)
             return HttpResponse("<h1>Deu erro no teu formulário</h1>")
 
    form = clienteForm() 
    context['form'] = form
    context['clientes'] = clientes
    return render(request, template_name, context) 
@login_required
def atualizar_cliente(request,id):
    try:
        cliente_ = cliente.objects.get(id=id)
    except cliente.DoesNotExist:
        return HttpResponse('<h1>Cliente não encontrado</h1>')
    
    if request.method == 'POST':
        form = clienteForm(request.POST, instance=cliente_)
        if form.is_valid():
            form.save()
            return redirect('novo_cliente')
        else:
            return HttpResponse('<h1>Erro na atualização do cliente</h1>') 
    form = clienteForm(instance=cliente_)
    template_name = 'novo_cliente.html'
    clientes = cliente.objects.all() 
    context = {
        'form': form,
        'clientes': clientes
    }
    return render(request, template_name, context)


@login_required
def excluir_cliente(request, id):
    try:
        cliente_ = cliente.objects.get(id=id)
        cliente_.delete()
    except cliente.DoesNotExist:
        return HttpResponse('<h1>Erro ao encontar o cliente. Não encontrado<h1>')   
    return redirect('novo_cliente')

def login_usuario(request):
    template_name = 'login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('novo_cliente')
        else:
            return HttpResponse(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    context = {'form': form}

    return render(request, template_name, context) 

def novo_usuario(request):
    template_name = 'novo_usuario.html'
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            f= form.save(commit=False)
            f.set_password(f.password)
            f.save()
            return redirect('login_usuario')
        else:
            return HttpResponse('Erro ao criar o usuário') 
    else:
        form = UsuarioForm()
    context = {'form': form}
    return render(request, template_name, context)    