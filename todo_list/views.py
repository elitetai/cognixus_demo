from social_django.utils import psa

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from todo_list.models import Todo
from todo_list.serializers import TodoSerializer

# OAuth
@api_view(['POST'])
@permission_classes([AllowAny])
@psa()
def register_by_access_token(request, backend):
    token = request.data.get('access_token')
    user = request.backend.do_auth(token)
    # print(request)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response(
            {'errors': {
                'token': 'Invalid token'
                }
            },
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'POST'])
def authentication_test(request):
    return Response({'message': "User successfully authenticated"}, status=status.HTTP_200_OK)

# To do list
class ListTodoAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodoAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UpdateTodoAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer