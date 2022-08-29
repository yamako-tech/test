from django.shortcuts import render
import datetime
from dateutil.parser import parse
from django.utils import timezone

from .models import HomeMessage

def index(request):

  # my_date = parse(my_date)
  # # my_date = datetime.strptime(my_date, '%Y-%m-%d')
  # msg = HomeMessage.objects.filter(start_date__gt=my_date, end_date__lt=my_date)
  # context['msg_list'] = msg

  context = {}
  # 1. get viewing date
  datas = HomeMessage.objects.all().values()
  # 本日の日付を取得
  my_date= datetime.date.today()
  # 投稿内容を全て取得
  msg = HomeMessage.objects.all().values()
  # 投稿期間中のものだけを表示
  msg2 = HomeMessage.objects.filter(start_date__lt=my_date, end_date__gt=my_date)

  context['msg_list'] = msg
  context['today'] = my_date
  context['dates'] = datas
  context['msg2'] = msg2

  print(HomeMessage.start_date)
  return render(request, 'index.html', context)



# 2. get start and end
# 3. Check if viewing date is between #2
# 4. If yes, the post is_published -- Show the post
# 5. If no, the post NOT is_publihed -- Hide the post

    # start_d = HomeMessage.start_date()
    # end_d = HomeMessage.end_date()
    # view_d = datetime.now()
    # date_from = datetime.datetime.strptime(request.GET['start_d'], '%Y-%m-%d %H:%M:%S')
    # start_date = datetime.strptime(request.GET['HomeMessage.start_date'], '%Y-%m-%d %H:%M:%S')
    # end_date = datetime.strptime(HomeMessage.end_date, '%Y-%m-%d %H:%M:%S')
    # view_date = datetime.now()
    # if end_date < view_date < start_date:
    #   msg = HomeMessage.objects.all().values()
    #   context['msg_list'] = msg
