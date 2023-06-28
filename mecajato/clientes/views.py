from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.get('carro')
        
        print(carros)
        
        
        return HttpResponse(f'O usuário {nome} {sobrenome} do email {email} e cpf {cpf} cadastrou o carro {carros}')
