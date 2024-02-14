from django.urls import path
from . views import *
urlpatterns = [
    path('addtodo',AddTodo.as_view(),name='addtodo'),
    path('deltodo<int:id>',delete,name='deltodo'),
    path('updatetodo<int:id>',Update.as_view(),name='uptodo'),
]
