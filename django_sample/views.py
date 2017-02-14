from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime

def search(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "searchpage.html", {"today" : today, "days_of_week" : daysOfWeek})


def searchresults(request):
   return render(request, "searchresults.html")

