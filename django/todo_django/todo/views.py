from django.shortcuts import render
from django.views.generic import View
from todo.models import Todo
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class TodoListView(View):
    def get(self, request):
        context = {
            'todo_list': Todo.objects.all()
        }
        return TemplateResponse(request, 'todo_list.html', context)
class TodoAddView(View):
    def get(self, request):
        return TemplateResponse(request, 'todo_add_list.html')
    def post(self, request):
       discription=request.POST['discription']
       fecha=request.POST['fecha']
       unidades=request.POST['unidades']
       Todo.objects.create(discription=discription, fecha=fecha, unidades=unidades)
       return HttpResponseRedirect('/')    
       

