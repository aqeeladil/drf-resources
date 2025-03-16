from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3

@api_view(['GET', 'POST'])
def drinks(request):
    db = boto3.resource('dynamodb', region_name='us-east-1')
    table = db.Table('drinks')

    if request.method == 'GET':
        drinks = table.scan()
        # return Response({'test': 'data'}, status=status.HTTP_200_OK)
        # return Response(drinks, status=status.HTTP_200_OK)
        return Response({'drinks': drinks['Items']}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        try:
            table.put_item(Item=request.data)
            return Response({'message': 'Drink added successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def drink(request, name):
    db = boto3.resource('dynamodb', region_name='us-east-1')
    table = db.Table('drinks')

    if request.method == 'GET':
        drink = table.get_item(Key={'name': name})
        if 'Item' in drink:
            return Response({'drink': drink['Item']}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Drink not found'}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        try:
            table.put_item(Item=request.data)
            return Response({'message': 'Drink updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        try:
            table.delete_item(Key={'name': name})
            return Response({'message': 'Drink deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    