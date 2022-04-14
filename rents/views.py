from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from . import serializers
from .models import Rent, User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model
from drf_yasg2.utils import swagger_auto_schema


User = get_user_model()


class RentCreateListView(generics.GenericAPIView):

    serializer_class = serializers.RentCreationSerializers
    queryset = Rent.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="List all rents made")
    def get(self, request):

        rents = Rent.objects.all()

        serializer = self.serializer_class(instance=rents, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Create a new rent")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentDetailView(generics.GenericAPIView):
    serializer_class = serializers.RentDetailSerializers
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="Retrieve an rent")
    def get(self, request, rent_id):

        rent = get_object_or_404(Rent, pk=rent_id)

        serializer = self.serializer_class(instance=rent)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an rent")
    def put(self, request, rent_id):
        data = request.data

        rent = get_object_or_404(Rent, pk=rent_id)

        serializer = self.serializer_class(data=data, instance=rent)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Remove/Delete an rent")
    def delete(self, request, rent_id):
        rent = get_object_or_404(Rent, pk=rent_id)

        rent.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRentsView(generics.GenericAPIView):
    serializer_class = serializers.RentDetailSerializers

    @swagger_auto_schema(operation_summary="Get all rent for a user")
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)

        rents = Rent.objects.all().filter(customer=user)

        serializer = self.serializer_class(instance=rents, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserRentDetail(generics.GenericAPIView):
    serializer_class = serializers.RentDetailSerializers

    @swagger_auto_schema(operation_summary="Get a user spesifics rent")
    def get(self, request, user_id, rent_id):
        user = User.objects.get(pk=user_id)

        rents = Rent.objects.all().filter(customer=user).get(pk=rent_id)

        serializer = self.serializer_class(instance=rents)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
