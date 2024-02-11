from django.urls import path
from . views import *
urlpatterns = [
    path('addtodo',AddTodo.as_view(),name='addtodo'),
]
