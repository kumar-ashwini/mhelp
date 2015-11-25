
""""
	category = request.data["category"]
	if not category:
		return send_response(ERROR_NO_CATEGORY, BAD_REQUEST)
    """
from django.shortcuts import render
from qanda.models import Answer, Question
from mothershelp.messages import *
from rest_framework.decorators import api_view
from qanda.serializers import *
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def create_question(request):
	if not user_authenticated(request):
		return send_response(ERROR_USER_NOT_AUTHENTICATED, UNAUTHORIZED)

	question = request.data["question"]
	if not question:
		return send_response(ERROR_NO_QUESTION, BAD_REQUEST)
    
	request.data["created_by"] = request.user.id
	serializers = QuestionSerializer(data=request.data)
	if serializers.is_valid():
		serializers.save()
		return send_response(QUESTION_CREATED, CREATED)

	return send_response(ERROR_SOMETHING_WRONG, BAD_REQUEST, serializers.errors)


@api_view(['POST'])
def create_answer(request):
	if not user_authenticated(request):
		return send_response(ERROR_USER_NOT_AUTHENTICATED, UNAUTHORIZED)

	question = request.data["question"]
	if not question:
		return send_response(ERROR_NO_QUESTION, BAD_REQUEST)

	text = request.data["text"]
	if not text:
		return send_response(ERROR_NO_ANSWER, BAD_REQUEST)

	request.data["created_by"] = request.user.id
	serializers = AnswerSerializer(data=request.data)

	if serializers.is_valid():
		serializers.save()
		return send_response(ANSWER_CREATED, CREATED, serializers.data)

	return send_response(ERROR_SOMETHING_WRONG, BAD_REQUEST, serializers.errors)

@api_view(['GET'])
def get_all_questions(request):
	data = Question.objects.all().order_by('-created_on')

	if len(data) == 0:
		return send_response(NO_QUESTION_POSTED, OK)

	serializers = QuestionResponseSerializer(data, many=True)
	question_data = {}
	question_data["questions"] = serializers.data
	return send_response(ALL_QUESTIONS, OK, question_data)
	#return send_response(ERROR_SOMETHING_WRONG, BAD_REQUEST, serializers.errors)

@api_view(['GET'])
def get_my_questions(request):
	if not user_authenticated(request):
		return send_response(ERROR_USER_NOT_AUTHENTICATED, UNAUTHORIZED)

	data = Question.objects.filter(created_by=request.user.id).order_by('-created_on')
	if len(data) == 0:
		return send_response(NO_QUESTION_POSTED, OK)

	serializers = QuestionSerializer(data, many=True)
	question_data = {}
	question_data["question"] = serializers.data
	return send_response(ALL_QUESTIONS, OK, question_data)

@api_view(['GET'])
def get_all_answer(request):

	question = request.GET.get('question')
	if not question:
		return send_response(ERROR_QUESTION_MISSING, BAD_REQUEST)
	data = Answer.objects.filter(question=question).order_by('created_on')
	if len(data) == 0:
		return send_response(NO_ANSWER_POSTED, OK)

	serializers = AnswerResponseSerializer(data, many=True)
	answer_data = {}
	answer_data["answer"] = serializers.data
	return send_response(ALL_ANSWER, OK, answer_data)


