from django.shortcuts import render, redirect
from django.http import HttpResponse

from todolist.models import TodoList, Category

def redirect_view(request):
    return redirect('/category')

def todo(request):
    todos = TodoList.objects.all()
    categories = TodoList.objects.all()

    if request.method == 'POST':
        if 'Add' in request.POST: 
            title = request.POST['description']
            date = str(request.POST['date'])
            category = request.POST['category_select']
            content = title + '--' + date + ' ' + category
            todo = TodoList(title=title, content=content, due_time=date, category=Category.objects.get(name=category))

            todo.save()
            return redirect('/todo')
        if 'Delete' in request.POST:
            checkedlist = request.POST.getlist('checkbox')

            for i in range(len(checkedlist)):
                todo = TodoList.objects.filter(id=int(checkedlist[i]))
                todo.delete()
    
    return render(request, 'todo.html', {'todo': todos, 'categories': categories})

def category(request):
    categories = Category.objects.all()
    
    if 'Add' in request.POST:
        name = request.POST['name']
        category = Category(name=name)
        category.save()
        return redirect('/category')
    
    if 'Delete' in request.POST:
        check = request.POST.getlist('check')

        for i in range(len(check)):
            categ = Category.objects.filter(id=int(check[i]))
            categ.delete()
        

    return render(request, 'category.html', {'categories': categories})
