from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('widgets/<int:widget_id>/create_widget/', views.CreateWidget, name='create_widget'),
  # path('widgets/<int:pk>/delete/', views.DeleteWidget.as_view(), name='delete_widget'),
]