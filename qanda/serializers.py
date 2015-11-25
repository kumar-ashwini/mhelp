""""
class CategorySerializer(serializers.ModelSerializer):
     
	class Meta:
		model = Category
"""


from rest_framework import serializers
from qanda.models import *
from account.serializers import MyUserResponseSerializer



class QuestionSerializer(serializers.ModelSerializer):
	#category=CategorySerializer()
	#category = serializers.SlugRelatedField(slug_field='name',many=True,read_only=True)
	class Meta:
		model = Question	
		

class QuestionResponseSerializer(serializers.ModelSerializer):
	created_by = MyUserResponseSerializer()
	class Meta:
		depth = 1
		model = Question

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer

class AnswerResponseSerializer(serializers.ModelSerializer):
	question = QuestionResponseSerializer()
	created_by = MyUserResponseSerializer()
	class Meta:
		depth = 1
		model = Answer
