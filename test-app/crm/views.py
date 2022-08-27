from django.shortcuts import render
from datetime import datetime,timedelta
from dateutil.parser import parse

from .models import HomeMessage

def index(request):
  context = {}
  my_date = request.POST.get('my_date','2022-08-24') # for eg. 2022-0826
  my_date = parse(my_date)
  # my_date = datetime.strptime(my_date, '%Y-%m-%d')
  msg = HomeMessage.objects.filter(start_date__gt=my_date, end_date__lt=my_date)
  context['msg_list'] = msg

  return render(request, 'index.html', context)

