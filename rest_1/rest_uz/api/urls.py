from django.urls import path
from rest_uz.api.views import movie_list, get_detail, todo_view

urlpatterns = [
    path('',movie_list,name=''),
    path('movie/<int:id>',get_detail,name='movie'),
    path('todo', todo_view, name='todo'),

]


