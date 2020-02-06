from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','code')

class CategoryRelationSerializer(serializers.ModelSerializer):
    child = CategorySerializer()

    class Meta:
        model = CategoryRelation
        fields = ('child',)