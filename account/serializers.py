from rest_framework import serializers
from account.models import *


class MyUserSerializer(serializers.ModelSerializer):
	#location = serializers.StringRelatedField(many = True)
	class Meta:
		model = MyUser
		exclude=('is_superuser', 'last_login', 'is_staff','user_permissions', 'groups', 'date_joined')

	def create(self, validated_data):
		user = MyUser(username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user


class MyUserResponseSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser
		fields = ('first_name', 'last_name', 'id', 'tag_line')

	
