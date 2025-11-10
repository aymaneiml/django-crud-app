from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        #get all the drikns
        drinksList = Drink.objects.all()
        #serialize them
        serializer = DrinkSerializer(drinksList, many=True)
        #return json
        return JsonResponse({"drinks": serializer.data}, safe=False)
    
    if request.method == 'POST':
        #deserialize data
        serializer = DrinkSerializer(data=request.data)
        #check if the date valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        oneDrink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = DrinkSerializer(oneDrink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(oneDrink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        ##if not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        oneDrink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
