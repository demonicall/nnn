from rest_framework import serializers
from todo_list.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta():
        model = ToDo
        fields = "__all__"
