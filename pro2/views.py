from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello World')


def wellcome(request):
    data = """<!DOCTYPE html><html><head><title>well come</title> </head> 
    <body><h1>Wellcome DJANGO</h1></body> </html>"""
    return HttpResponse(data)