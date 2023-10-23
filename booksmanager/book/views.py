from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def book_list(request: HttpRequest):
    return HttpResponse("booklist")
