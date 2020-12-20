from rest_framework import serializers
from .models import pizzaModel,pizzaSize,typeOfPizza

class PizzaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = pizzaModel
        fields = ['id', 'typeOfPizza', 'sizeOfPizza', 'toppingOfPizza']
        