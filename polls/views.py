import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers

from polls.models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def test(request):
    if request.method == "GET":
        dic = {}
        result = serializers.serialize("json",Question.objects.all())
        # L = JsonResponse(list(result), safe=False)
        # result = serializers.serialize("json", result)
        # print(serializers.serialize("json", result))
        dic['code'] = '1'
        dic['message'] = ''
        dic['result'] = result
        return HttpResponse(result)
