from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingred
from .serializers import RecipeSerializer, IngredSerializer

from rest_framework import status


class RecipeAPIView(APIView):

    def get(self, request):
        recipes = Recipe.objects.all()
        serializers = RecipeSerializer(recipes, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = RecipeSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


class RecipeDetails(APIView):

    def get_object(self, id):
        try:
            return Recipe.objects.get(id=id)

        except Recipe.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        recipe = self.get_object(id)
        serializers = RecipeSerializer(recipe)
        return Response(serializers.data)

    def put(self, request, id):
        recipe = self.get_object(id)
        serializers = RecipeSerializer(recipe, data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recipe = self.get_object(id)
        recipe.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# class RecipeView(APIView):
#     def get(self, request, **kwargs):
#         if kwargs.get('recipe_id') is None:
#             recipe_serializer = RecipeSerializer(
#                 Recipe.objects.all(), many=True)
#             return Response(recipe_serializer.data, status=200)
#         else:
#             recipe_id = kwargs.get('recipe_id')
#             recipe_serializer = RecipeSerializer(
#                 get_object_or_404(Recipe, id=recipe_id))
#             return Response(recipe_serializer.data, status=200)

class IngredView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('ingred_id') is None:
            ingred_serializer = IngredSerializer(
                Ingred.objects.all(), many=True)
            return Response(ingred_serializer.data, status=200)
        else:
            ingred_id = kwargs.get('ingred_id')
            ingred_serializer = IngredSerializer(
                get_object_or_404(Ingred, id=ingred_id))
            return Response(ingred_serializer.data, status=200)
