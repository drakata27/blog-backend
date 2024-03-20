from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import *

from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Auth
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def test_endpoint(request):
    if request.method == 'GET':
        data = f"Hey {request.user}, you are seeing a GET response"
        return Response( {'response':data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f"Hey {request.user}, this is POST data and your text is {text}"
        return Response( {'response':data}, status=status.HTTP_200_OK)
    return Response( {}, status=status.HTTP_400_BAD_REQUEST)

# Blogs
@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/blog/',
            'method': 'GET',
            'title': None,
            'body': None,
            'description': 'Returns an array of blog'
        },
        {
            'Endpoint': '/blog/id',
            'method': 'GET',
            'title': None,
            'body': None,
            'description': 'Returns a single blog object'
        },
        {
            'Endpoint': '/blog/create/',
            'method': 'POST',
            'title': {'title': ""},
            'body': {'body': ""},
            'description': 'Creates new blog with data sent in post request'
        },
        {
            'Endpoint': '/blog/id/update/',
            'method': 'PUT',
            'title': {'title': ""},
            'body': {'body': ""},
            'description': 'Creates an existing blog with data sent in post request'
        },
        {
            'Endpoint': '/blog/id/delete/',
            'method': 'DELETE',
            'title': None,
            'body': None,
            'description': 'Deletes an exiting blog'
        },
        # Auth
        {
            'Endpoint': 'token/',
            'method': '',
            'title': None,
            'body': None,
            'description': 'Token'
        },
        {
            'Endpoint': '/api/token/refresh/',
            'method': '',
            'title': None,
            'body': None,
            'description': 'Refreshes the user token'
        },
        {
            'Endpoint': 'test/',
            'method': '',
            'title': None,
            'body': None,
            'description': 'Test Endpoint'
        },
    ]

    return Response(routes)

@api_view(['GET', 'POST'])
def get_blogs(request):
    if request.method == 'GET':
        return get_blogs_list()
    
    if request.method == 'POST':
        return create_blog(request)

@api_view(['GET', 'DELETE'])
def get_blog(request, pk):
    if request.method == 'GET':
        return get_blog_detail(pk)
    
    if request.method == 'DELETE':
        return delete_blog(request, pk)
    
@api_view(['PUT', 'GET'])
def update_blog(request, pk):
    return update_blog_details(request, pk)
