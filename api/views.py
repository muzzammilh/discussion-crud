from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

class PostApiView(APIView):

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



class PostEditApiView(APIView):

    #3. Update post
    def put(self, request, post_id):
        '''
        Updates the posts item with given post_id if exists
        '''
        post = Post.objects.filter(id=post_id, user = request.user.id).first()
        if post is None:
            return Response(
                {'res': 'Object with requested id does not exists'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'user': request.user.id,
            'body': request.data.get('body')
        }
        serializer = PostSerializer(instance = post, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #3. Delete post
    def delete(self, request, post_id):
        '''
        Deletes the posts item with given post_id if exists
        '''
        post = Post.objects.filter(id=post_id, user = request.user.id).first()
        if post is None:
            return Response(
                {'res': 'Post with requested id does not exists'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        post.delete()

        return Response({'res': 'Post deleted'}, status=status.HTTP_200_OK)
