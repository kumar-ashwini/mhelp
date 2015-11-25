from rest_framework.decorators import api_view
from account.models import MyUser
from account.serializers import *
from django.core.exceptions import ObjectDoesNotExist
from mothershelp.messages import *
from django.forms import model_to_dict

# Create your views here.


@api_view(['POST'])
def create_user(request):
    username = request.POST.get(MYUSER_USERNAME)
    if not username:
        return send_response(ERROR_USERNAME_REQUIRED, BAD_REQUEST)

    password = request.POST.get(MYUSER_PASSWORD)
    if not password:
        return send_response(ERROR_PASSWORD_REQUIRED, BAD_REQUEST)

    confirm_password = request.POST.get(MYUSER_CONFIRM_PASSWORD)
    if not confirm_password:
        return send_response(ERROR_CONFIRM_PASSWORD_REQUIRED, BAD_REQUEST)

    if confirm_password != password:
        return send_response(ERROR_PASSWORD_DO_NOT_MATCH, BAD_REQUEST)

    myuser = MyUser.objects.all()
    for user in myuser:
        if user.username == username:
            return send_response(ERROR_USERNAME_ALREADY_EXIST, BAD_REQUEST)

    serializer = MyUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data["is_active"] = True
        serializer.save()
        return send_response(USER_CREATED, CREATED)

    return send_response(ERROR_SOMETHING_WRONG, BAD_REQUEST, serializer.errors)


@api_view(['POST'])
def update_user_profile(request):

    if not user_authenticated(request):
        return send_response(ERROR_USER_NOT_AUTHENTICATED, UNAUTHORIZED)

    try:
        user = MyUser.objects.get(id=request.user.id)
    except:
        return send_response(ERROR_NO_SUCH_USER_EXIST, BAD_REQUEST)

    first_name = request.POST.get(MYUSER_FIRST_NAME)
    if first_name:
    	first_name = first_name.strip().capitalize()
    	user.first_name = first_name

    last_name = request.POST.get(MYUSER_LAST_NAME)
    if last_name:
    	last_name = last_name.strip().capitalize()
    	user.last_name = last_name

    age = request.POST.get(MYUSER_AGE)
    if age:
        user.age = age

    tag_line = request.POST.get(MYUSER_TAGLINE)
    if tag_line:
        user.tag_line = tag_line

    gender = request.POST.get(MYUSER_GENDER)
    if gender:
        user.gender = gender
    try:
        user.save()
    except:
        return send_response(ERROR_SOMETHING_WRONG, BAD_REQUEST)

    user = MyUser.objects.get(id=request.user.id)

    data = model_to_dict(user, fields=[MYUSER_USERNAME, MYUSER_TAGLINE, MYUSER_GENDER, MYUSER_AGE])

    data[MYUSER_NAME] = user.get_full_name()
    return send_response(PROFILE_UPDATED, OK, data)


@api_view(['GET'])
def get_user(request):

    if not user_authenticated(request):
        return send_response(ERROR_USER_NOT_AUTHENTICATED, UNAUTHORIZED)

    try:
        user = MyUser.objects.get(id=request.user.id)
    except ObjectDoesNotExist:
        return send_response(ERROR_NO_SUCH_USER_EXIST, NOT_FOUND)

    data = model_to_dict(user, fields=[ID, MYUSER_USERNAME, MYUSER_TAGLINE,
                                       MYUSER_GENDER, MYUSER_AGE])

    data[MYUSER_NAME] = user.get_full_name()

    return send_response(PROFILE_FOUND, OK, data)
