from rest_framework import generics, permissions
from .models import Todo
from .pagination import CustomPagination
from .serializers import TodoSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["ToDo"], request=TodoSerializer, responses={200: TodoSerializer(many=True)})
class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
@extend_schema(tags=["ToDo"], request=TodoSerializer, responses={200: TodoSerializer})
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
