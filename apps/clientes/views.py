from django.shortcuts import render, redirect 
from django.http import HttpResponse

from .forms import clienteForm
from .models import cliente

# Create your views here.

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


def excluir_cliente(request, id):
    try:
        cliente_ = cliente.objects.get(id=id)
        cliente_.delete()
    except cliente.DoesNotExist:
        return HttpResponse('<h1>Erro ao encontar o cliente. Não encontrado<h1>')   
    return redirect('novo_cliente')
