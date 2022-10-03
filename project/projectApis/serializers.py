from rest_framework import serializers
from projectApis.models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'assignedDate', 'resource', 'priority', 'description']