from rest_framework import serializers
from crm.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ( 'id', 'username', 'first_name', 'last_name' )
        fields = '__all__' # manda llamar todos los campos
        read_only_fields = ('id', )