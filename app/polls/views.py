from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    ctx = {
        "greetings": "Hello, three!",
        "location": {
            "city": "Seoul",
            "country": "South Korea",
        },
        "languages": ["Korean", "English"],
    }
    return render(request, "polls/main.html", context=ctx)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
