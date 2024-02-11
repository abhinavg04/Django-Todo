from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def todoView(request):
    return render(request,'todo_list.html')

class AddTodo(View):
    def get(self,request):
        return render(request,'add_todo.html')