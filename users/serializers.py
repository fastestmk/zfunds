from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('id','username','is_superuser','first_name', 'last_name')
        fields = "__all__"
