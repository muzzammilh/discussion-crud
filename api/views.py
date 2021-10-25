from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

class PostListApiView(APIView):

    # 1. List all
    def get(self, request):
        '''
        List all the post items
        '''
        posts = Post.objects.all().order_by('created_at')
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Create New
    def post(self, request):
        '''
        Add new post item
        '''
        data = {
            'user': request.user.id,
            'body': request.data.get('body')
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)