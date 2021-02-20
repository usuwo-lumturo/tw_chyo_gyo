from django.shortcuts import render
from django.http      import HttpResponse
import calendar

# Create your views here.
def index(request):
    lc = calendar.HTMLCalendar()
    body = lc.formatyear(2020, width=4)
    return render(request, 'gyogyo/index.html')