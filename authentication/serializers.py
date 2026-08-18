from rest_framework import serializers
from .models import Product

class ProductSerializer( serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = '__all__'

        # exploiting the fileds that we have to show
        fields =[
            "id",
            "name",
            "price"
        ]

        # some fileds doesnot have to be changed 
        read_only_fields = ("id","name")


