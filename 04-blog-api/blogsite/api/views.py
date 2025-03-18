from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView


# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    lookup_field = 'pk'


# class BlogPostList(APIView):
#     def get(self, request):
#         blogposts = BlogPost.objects.all()
#         serializer = BlogPostSerializer(blogposts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BlogPostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BlogPostList(APIView)
#     def get(self, request, format=None):
#         title = request.query_params.get('title', '')

#         if title:
#             blogposts = BlogPost.objects.filter(title__icontains=title)
#         else:
#             blogposts = BlogPost.objects.all()

#         serializer = BlogPostSerializer(blogposts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

