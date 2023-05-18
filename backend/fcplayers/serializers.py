from rest_framework import serializers
from .models import Fcplayers

class FcplayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fcplayers
        fields = ['id', 'firstname', 'lastname', 'age', 'parent_id']
        depth = 1