from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import BookSerializer
from .models import book

# Create your views here.


@api_view(["GET"])
def booklist(request):
    books = book.objects.all()
    serializedData = BookSerializer(books, many=True).data
    return Response(serializedData)


@api_view(["POST"])
def createBook(request):
    data = request.data
    serializedData = BookSerializer(data=data)
    if serializedData.is_valid():
        serializedData.save()
        return Response(serializedData.data, status=status.HTTP_201_CREATED)
    return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
