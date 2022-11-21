from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task



#shows list of tasks on landing page
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'toDoList/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context




    
#shows specific task on dummy page
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'toDoList/dummy.html'

#adds a task on add page
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'toDoList/add.html'

#delete task on landing page
class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'toDoList/update.html'
    

#def index(request):
    #return render(request, 'toDoList/index.html')


#def toDoList(request):
    #return render(request, 'toDoList/index.html')

#def dummy(request):
    #return render(request, 'toDoList/dummy.html')





#def add(request):
    #return render(request, 'toDoList/add.html')



#def update(request):
    #return render(request, 'toDoList/update.html')


