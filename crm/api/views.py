from rest_framework import generics
from crm.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class UsersAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
