from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from cadastro.models import Cadastro
from cadastro.serializers import CadastroSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def cadastro_list(request):

    if request.method == 'GET':
        cadastro = Cadastro.objects.all()
        
        cadastro_serializer = CadastroSerializer(cadastro, many=True)
        return JsonResponse(cadastro_serializer.data, safe=False)
        
    elif request.method == 'POST':
        cadastro_data = JSONParser().parse(request)
        cadastro_serializer = CadastroSerializer(data=cadastro_data)
        if cadastro_serializer.is_valid():
            cadastro_serializer.save()
            return JsonResponse(cadastro_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(cadastro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Cadastro.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def cadastro_detail(request, pk):
    cadastro = Cadastro.objects.get(pk=pk)
    if request.method == 'GET': 
        cadastro_serializer = CadastroSerializer(cadastro) 
        return JsonResponse(cadastro_serializer.data) 
    elif request.method == 'PUT': 
        cadastro_data = JSONParser().parse(request) 
        cadastro_serializer = CadastroSerializer(cadastro, data=cadastro_data) 
        if cadastro_serializer.is_valid(): 
            cadastro_serializer.save() 
            return JsonResponse(cadastro_serializer.data) 
        return JsonResponse(cadastro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    if request.method == 'DELETE': 
        cadastro.delete() 
        return JsonResponse({'mensagem': 'O cadastro foi deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
 

    
