from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CategoryModel, BlogModel
from .serializers import CategorySerializer, BlogSerializer




class CategoryView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer



class BlogView(ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


