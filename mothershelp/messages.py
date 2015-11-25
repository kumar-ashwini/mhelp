from rest_framework.response import Response
from rest_framework import status

ID = "id"
#MyUser
MYUSER_GENDER = "gender"
MYUSER_NAME = "name"
MYUSER_AGE = "age"
MYUSER_TAGLINE = "tag_line"
MYUSER_USERNAME = "username"
MYUSER_FIRST_NAME = "first_name"
MYUSER_LAST_NAME = "last_name"
MYUSER_PASSWORD = "password"
MYUSER_CONFIRM_PASSWORD = "confirm_password"

#category

CATEGORY_NAME = "name"

#Question
QUESTION_QUESTION = "question"
QUESTION_CATEGORY = "category"
QUESTION_CREATEDBY = "created_by"

#Answer
ANSWER_TEXT = "text"
ANSWER_QUESTION = "question"
ANSWER_CREATEDBY = "created_by"

#Errors
ERROR_USER_NOT_AUTHENTICATED = "user not authenticated"
ERROR_USERNAME_REQUIRED = "username is required"
ERROR_PASSWORD_REQUIRED = "password is required"
ERROR_PASSWORD_DO_NOT_MATCH = "password do not match"
ERROR_CONFIRM_PASSWORD_REQUIRED = "confirm password is required"
ERROR_USERNAME_ALREADY_EXIST = "username already exist"
ERROR_NO_SUCH_USER_EXIST = "no such user exist"
ERROR_SOMETHING_WRONG = "something went wrong try again later"
ERROR_NO_ANSWER = "No answer given"
ERROR_QUESTION_MISSING = "question missing"
ERROR_NO_QUESTION = "No question provided"
ERROR_NO_CATEGORY = "Atleast one category should be there"


#Positive messages
USER_CREATED = "New User Created"
ANSWER_CREATED = "Answer successfully posted"
PROFILE_UPDATED = "Profile updated successfully"
PROFILE_FOUND = "Profile found"
QUESTION_CREATED = "Question successfully posted"
ALL_QUESTIONS = "All questions latest first"
NO_QUESTIONS_POSTED = "No questions available"
ALL_ANSWER = "All answers latest first"
NO_ANSWER_POSTED = "No answer available"

#status constants
UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
BAD_REQUEST = status.HTTP_400_BAD_REQUEST
CREATED = status.HTTP_201_CREATED
NOT_FOUND = status.HTTP_404_NOT_FOUND
OK = status.HTTP_200_OK


def send_response(message, response_code, data=None):

    if data is None:
        data = {}

    data['message'] = message
    return Response(data, status=response_code)


def user_authenticated(request):
    anon = request.user.is_anonymous()
    return not anon
