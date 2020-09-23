from django.urls import path
from .views import ListTodo,DetailTodo

urlpatterns=[
    path('<int:pk>/',DetailsTodo.as_view()),
    path('',ListTodo.as_view()),
]