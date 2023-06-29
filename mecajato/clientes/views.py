from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Carro

def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')
        
        print(nome, sobrenome, email, cpf, carros, placas, anos) 

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf   
        )
        
        cliente.save()
        
        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save() #TODO resolver problema com db
        
        
        return HttpResponse(f'O usuário {nome} {sobrenome} do email {email} e cpf {cpf} cadastrou o(s) carro(s) {carros} com as placas {placas} com os anos {anos}')
