from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # User model django thanne provide cheyyunnathan so models.pyil nammal User model create cheyyanda User model serializer.pyil use cheyyumbo preferred fields kodkam
        fields=['username','password','email']
        # User model django provide cheyyunna model aan athile all fields namuk venda so namak vendunna fields edthu
        extra_kwargs = {'password': {'write_only': True}}
        # password write only kodthal response verumbol password kaaniklla
        # ivide extra_kwargs means nammale field'l nthelum extra details kodkan use cheyyam.

        # user register cheyyumbol account create aakanulla function
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        # short form for validated_data['username'],validated_data['email'],validated_data['password']