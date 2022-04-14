from .models import Rent
from rest_framework import serializers


class RentCreationSerializers(serializers.ModelSerializer):
    title = serializers.CharField(default='BUKU_JONI')
    author = serializers.CharField(default='JONI')
    photo = serializers.CharField(default='BUKU_JONI.png')

    class Meta:
        model = Rent
        fields = ['id', 'title', 'author', 'photo']
        # fields = ['id', 'title', 'author']


class RentDetailSerializers(serializers.ModelSerializer):
    title = serializers.CharField(default='BUKU_JONI')
    author = serializers.CharField(default='JONI')
    photo = serializers.CharField(default='BUKU_JONI.png')
    borrowed_on = serializers.DateTimeField()

    class Meta:
        model = Rent
        fields = ['id', 'title', 'author',
                  'photo', 'borrowed_on']
