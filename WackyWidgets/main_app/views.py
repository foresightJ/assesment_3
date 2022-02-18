from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm
from .models import Widget

def home(request, widget_id):
    widgets = Widget.objects.all()
    widget_id = Widget.objects.get(id=widget_id)
    widget_form = WidgetForm()
    return render(request, 'home.html', {"my_widget": widgets, "widget_form":widget_form})

def add_widget(request, cat_id):
  pass
# Create your views here.
class CreateWidget(CreateView):
  model = Widget
  fields = '__all__'
#   success_url = '/widgets/'
class DeleteWidget(CreateView):
  model = Widget
  fields = '__all__'
#   success_url = '/widgets/'