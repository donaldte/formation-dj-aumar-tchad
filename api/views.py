import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Action, Reference
from rest_framework.decorators import api_view
from .serializers import ActionSerializer, ReferenceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


# @csrf_exempt
# def home(request): 
#     if request.method == 'POST':
#         print(request.body)
#         data = json.loads(request.body)
#         name = data['name']
#         description = data['description']
#         action = Action.objects.create(name=name, description=description)
#         return JsonResponse({'message': 'Action created successfully', 'action': action.name})  
    
#     actions = Action.objects.all()
#     data = [{'name': action.name, 'description': action.description} for action in actions]  
#     return JsonResponse(data, safe=False)

@api_view(['GET', 'POST'])
def home(request):
    data = request.data
    
    if request.method == 'POST':
        serializer = ActionSerializer(data=data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    actions = Action.objects.all()
    serializer = ActionSerializer(actions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def reference_api_view(request):
    references = Reference.objects.all()
    serializer = ReferenceSerializer(references, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



class ActionViewSet(ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    
    
    
"""
Relation 
permission,
authentification
throuttle
pagination
documentation
"""