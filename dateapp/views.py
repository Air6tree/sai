from django.shortcuts import render
from django.http import HttpResponse
import datetime as date

# Create your views here.
def display(request):
  date1 = date.datetime.now()
  # date = datetime.datetime.now()
  return HttpResponse(date1)