from django.shortcuts import render, HttpResponse

# Create your views here.

# def homepage(request):
#     return HttpResponse("Hello World")

# def homepage(request):
#     return HttpResponse("Hello world")

    

def homepage(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")

def tes(request):
    return HttpResponse("test 2 page")



