from django.shortcuts import render
from datetime import datetime

from .models import HomeMessage

def index(request):
  context = {}
  start = HomeMessage.start_date.objects.all()
  end = HomeMessage.end_date.objects.all()
  now = datetime.now()
  if now is between start and end:
    msg = HomeMessage.message.objects.all().values()
    context['msg_list'] = msg

    return render(request, 'index.html', context)

