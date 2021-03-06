from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo



    

def homepage(request):
    return render(request, "index.html")




def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "books.html", {"todo_list": todo_list})
 
 
def add_todo(request):
    form = request.POST
    text = form["todo-text"]
    todo = ToDo(text=text)
    todo.save()

    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)  
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)  
    todo.is_favorite = True
    todo.save()
    return redirect(test)    

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)  
    todo.is_favorite = False
    todo.save()
    return redirect(test)    


def close_todo(request, id):
    todo = ToDo.objects.get(id=id)  
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)  

# def test(request):
#     return HttpResponse("test 2 page")

# def test(request):
#      return render(request, "dgtest1.html")

# def test(request):
#      return render(request, "dgtest2.html")

# def test(request):
#      return render(request, "dgtest3.html")




