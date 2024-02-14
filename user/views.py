from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from . models import TodoModel
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
class TodoView(View):
    def get(self,request):
        model = TodoModel.objects.all()
        return render(request,'todo_list.html',{'data':model})
    # def post(self,request):
    #     print(request.POST)
    #     form = TodoForm(initial={'title':request.POST.get('inp')})
    #     return render(request,'add_todo.html',{'form':form})

class AddTodo(View):
    def get(self,request):
        form = TodoForm()
        return render(request,'add_todo.html',{'form':form})
    def post(self,request):
        form_data = TodoForm(data=request.POST,files=request.FILES)
        print('hai')
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Successfully Submitted')
            return redirect('todolist')
        else:
            messages.error(request,"Failed")
            return render(request,'add_todo.html',{'form':form_data})
        
def delete(request,id):
    model = TodoModel.objects.get(id=id)
    model.delete()
    messages.error(request,"SuccessFully Deleted")
    return redirect('todolist')

class Update(View):
    def get(self,request,id):
        model = TodoModel.objects.get(id=id)
        form = TodoForm(instance=model)
        return render(request,'update.html',{"form":form})