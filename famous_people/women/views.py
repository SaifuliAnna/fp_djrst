from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


# 5_________
class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:  # if pk is None:
           return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:  # if pk is None:
           return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        instance.delete()

        return Response({"post": f"delete post {str(pk)}"})


# # 4_________
# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#
#         return Response({'post': WomenSerializer(post_new).data})
#

# 2_________
# class WomenAPIView(APIView):
#     def get(self, request):
#         lst = Women.objects.all()
#         return Response({'title': 'Angelina Jolie'})
#
#     def post(self, request):
#         return Response({'title': 'Jenife Lopes'})


# 3_________
# class WomenAPIView(APIView):
#     def get(self, request):
#         lst = Women.objects.all().values()
#         return Response({'posts': list(lst)})
#
#     def post(self, request):
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#
#         return Response({'post': model_to_dict(post_new)})


# 1_________
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer