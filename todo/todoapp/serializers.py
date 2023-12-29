from rest_framework import serializers
from .models import Todo
#we using class meta because we'll have many models and their descriptions
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=('id','title','description','completed')