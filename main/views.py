from django.shortcuts import render, HttpResponse
from .models import ToDo



    

def homepage(request):
    return render(request, "index.html")




def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})
 
 


# def test(request):
#     return HttpResponse("test 2 page")

# def test(request):
#      return render(request, "dgtest1.html")

# def test(request):
#      return render(request, "dgtest2.html")

# def test(request):
#      return render(request, "dgtest3.html")




