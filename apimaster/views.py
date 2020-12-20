from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import *
from .serializers import PizzaModelSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET', 'PUT', 'DELETE'])
def deletePizza(request, pk):
    try: 
        pizzaToDel = pizzaModel.objects.get(pk=pk) 
        pizzaToDel.delete()
        return JsonResponse({'message':'The pizza is deleted '})
    except pizzaModel.DoesNotExist: 
        return JsonResponse({'message': 'The pizza does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET','DELETE','POST'])

def createPizza(request):
    if request.method=='POST':
        p_size = pizzaSize.objects.all()
        allowed_size = []
        for i in p_size:
            allowed_size.append(i.sizeOfPizza)
        allowed_types = ['Regular ','Square']
        #############################################
        pizzaData = JSONParser().parse(request)
        pizza_serializer = PizzaModelSerializer(data = pizzaData)
        
        if pizza_serializer.is_valid():
            
            if pizza_serializer.validated_data['typeOfPizza'] in allowed_types  :
                if pizza_serializer.validated_data['sizeOfPizza'] in allowed_size:
                    pizza_serializer.save()
                    return JsonResponse(pizza_serializer.data, status=status.HTTP_201_CREATED) 
                else:
                    return JsonResponse({'message': 'WRONG DATA'}, status=status.HTTP_412_PRECONDITION_FAILED) 
                
            else:
                return JsonResponse({'message': 'WRONG DATA'}, status=status.HTTP_412_PRECONDITION_FAILED) 
                
        return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return 
    else:
        pizza = pizzaModel.objects.all()
        pizza_serializer =PizzaModelSerializer(pizza,many= True)
        return JsonResponse(pizza_serializer.data,safe=False) 

@api_view(['GET'])
def listPizza(request):
    pizza = pizzaModel.objects.all()
    if request.method=='GET':
        pizza_serializer = PizzaModelSerializer(pizza,many=True)
        return JsonResponse(pizza_serializer.data,safe=False)
    
@api_view(['GET'])
def filterBySize(request,size):
    pizza = pizzaModel.objects.filter(sizeOfPizza=size)

    if request.method=='GET':
        pizza_serializer = PizzaModelSerializer(pizza,many=True)
        return JsonResponse(pizza_serializer.data,safe=False)

  
@api_view(['GET'])
def filterByType(request,typeOfPizza):
    pizza = pizzaModel.objects.filter(typeOfPizza=typeOfPizza)

    if request.method=='GET':
        pizza_serializer = PizzaModelSerializer(pizza,many=True)
        return JsonResponse(pizza_serializer.data,safe=False)

@api_view(['PUT'])
def updatePizza(request,pk):
    pizza = pizzaModel.objects.get(id =pk)
    print(pizza)
    if request.method=='PUT':
        pizza_update = JSONParser().parse(request) 
        pizza_serializer = PizzaModelSerializer(pizza, data=pizza_update) 
        if pizza_serializer.is_valid(): 
            pizza_serializer.save() 
            return JsonResponse(pizza_serializer.data) 
        return JsonResponse(pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

