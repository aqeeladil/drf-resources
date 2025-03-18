from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.paginator import Paginator

class PublicBlogView(APIView):
    
        def get(self, request):
            try:
                blogs = Blog.objects.all()
                if request.GET.get('search'):
                    # blogs = blogs.filter(title__icontains=request.GET.get('search'))
                    blogs = blogs.filter(Q(title__icontains=request.GET.get('search')) | Q(content__icontains=request.GET.get('search')))
    
                # pagination
                page_number = int(request.GET.get('page', 1))
                paginator = Paginator(blogs, 10)
                page_obj = paginator.get_page(page_number)  
                serializer = BlogSerializer(page_obj, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            
                # page_size = int(request.GET.get('size', 10))
                # start_index = (page_number - 1) * page_size
                # end_index = page_number * page_size
                # return Response(serializer.data[start_index:end_index])
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
           
            
class BlogView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            user = request.user
            request.data['user'] = user.id
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, message='Blog created successfully', status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            user = request.user
            blogs = Blog.objects.filter(user=user)
            if request.GET.get('search'):
                # blogs = blogs.filter(title__icontains=request.GET.get('search'))
                blogs = blogs.filter(Q(title__icontains=request.GET.get('search')) | Q(content__icontains=request.GET.get('search')))

            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetailView(APIView):
        
        permission_classes = [IsAuthenticated]
        authentication_classes = [JWTAuthentication]
    
        def get(self, request, pk):
            try:
                blog = Blog.objects.get(id=pk)
                serializer = BlogSerializer(blog)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        def put(self, request):
            try:
                blog = Blog.objects.filter(uid=request.data.get('uid'))
                serializer = BlogSerializer(blog, data=request.data)
                if blog.DoesNotExist():
                    return Response({'error': 'Blog does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                if request.user.id == blog.user.id:
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'error': 'You are not allowed to update this blog'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
        def delete(self, request):
            try:
                blog = Blog.objects.filter(uid= request.data.get('uid'))
                if blog.DoesNotExist():
                    return Response({'error': 'Blog does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                if request.user.id == blog.user.id:
                    blog.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            