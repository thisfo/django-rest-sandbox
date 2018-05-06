from django.contrib.auth.models import User
from project.api.models import Project
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ('url', 'title', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

