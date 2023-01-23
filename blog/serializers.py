from rest_framework import serializers
from .models import CategoryModel, BlogModel

 
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryModel
        fields = (
            "id",
            "name"
        )
    


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    
    class Meta:
        model = BlogModel
        fields = (
            "id",
            "title",
            "description",
            "category",
            "category_id",
            "is_published",
            "created_date",
            "updated_date"
        )