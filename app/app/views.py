from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("hello world")


def error_404_view(request, exception):
    return HttpResponseNotFound("페이지를 찾을 수 없습니다.!")
