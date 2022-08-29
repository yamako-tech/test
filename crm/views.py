from django.shortcuts import render
import datetime
from .models import HomeMessage

def index(request):
  context = {}
  # Get today's date
  my_date= datetime.date.today()
  
  # Filter by is_publishe, start_date and end_date
  msg = HomeMessage.objects.filter(is_published=True, start_date__lt=my_date, end_date__gt=my_date)

  context['msg_list'] = msg

  return render(request, 'index.html', context)

