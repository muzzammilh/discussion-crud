from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class PostListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request):
        '''
        List all the todo items for given requested user
        '''
        # todos = Todo.objects.filter(user = request.user.id)
        # serializer = TodoSerializer(todos, many=True)
        return Response({"dist": "hello world"}, status=status.HTTP_200_OK)