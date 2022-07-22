from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("<h1 style=\"color: blue\">Hello, World!</h1>")

def victor(request):
	return HttpResponse("Hello, Victor!")

def multiply(request):
	a = 3
	b = 3
	c = a * b
	return HttpResponse(
	f"{a} x {b} = {c}"
	)

def x(request):
	return render(request, "hello/x.html")
