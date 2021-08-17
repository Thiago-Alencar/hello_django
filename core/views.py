from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos.</h1>'.format(nome, idade))

def soma(request, valor1,valor2):
    return HttpResponse('Soma {} + {} = {}.'.format(valor1,valor2,valor1+valor2))
def div(request, valor1,valor2):
    if valor2>0:
      valor3=  valor1 / valor2
    else: valor3 = 'Não pode dividir por zero'
    return HttpResponse('Divisão {} / {} = {}.'.format(valor1,valor2,valor3))

def sub(request, valor1,valor2):
    return HttpResponse('Subtração {} - {} = {}.'.format(valor1,valor2,valor1-valor2))

def mult(request, valor1,valor2):
    return HttpResponse('Multiplicação {} x {} = {}.'.format(valor1,valor2,valor1*valor2))



