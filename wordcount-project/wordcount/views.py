from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Hello')


def eggs(request):
    return HttpResponse('<h1>Eggs</h1>')