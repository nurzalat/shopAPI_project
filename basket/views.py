from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response

from basket import serializers
from rest_framework.views import APIView


class BasketApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
        serializer = serializers.BasketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
