from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class UserAPIView(RetrieveAPIView):
    permissions_classes = (IsAuthenticated,)
    # serializer_class = UserSerializer

    @staticmethod
    def get(request):
        context = {}
        try:
            qs = User.objects.get(username=request.user.username)
            serializer = UserSerializer(qs)
            context["success"] = True
            context["user"] = serializer.data
        except Exception as e:
            print("erorrrrrrrrrrrrrrrrrr", str(e))
            context["success"] = False
            context["msg"] = "some error"
        return Response(context)