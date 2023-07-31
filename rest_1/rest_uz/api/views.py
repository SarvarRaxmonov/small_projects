from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_uz.models import Movie
from django.http import JsonResponse
from rest_uz.models import Todo
from .serializers import TodoSerializer

def movie_list(request):
    movies = Movie.objects.all()
    data = {"data": list(movies.values())}
    return JsonResponse(data)

def get_detail(request, id):
    movie = Movie.objects.filter(id=id)
    data = {"data": list(movie.values())}
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def todo_view(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


