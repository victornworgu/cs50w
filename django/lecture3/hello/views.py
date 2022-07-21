from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, World!")

def victor(request):
	return HttpResponse("Hello, Vctor!")

def multiply(request):
	a = 3
	b = 3
	c = a * b
	return HttpResponse(
	f"{a} x {b} = {c}"
	)
