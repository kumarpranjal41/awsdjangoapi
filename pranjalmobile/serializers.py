from pranjalmobile.models import signup
from rest_framework import serializers
from pranjalmobile.models import signup


class signupSerializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = "__all__"     # ['name' ,'email']