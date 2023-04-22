from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer


# 8_________
class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all() якщо 17 строчка є то цієї не потрібно і в юрлсах треба змінити
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)


    # @action(methods=['get'], detail=False)
    # def category(self, request):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})


    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
