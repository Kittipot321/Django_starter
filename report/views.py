from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from main.models import *

# รายงานว่าจะให้ดูเป็นวัน สัปดาห์ เดือน ปี
@login_required
def report_filters(request,filters_select):
    total = 0
    order = Order.objects.all().order_by('-date_time')
    if filters_select == 'day':
        page_title = 'Report(Day)'
        order = order.filter(date_time__day=datetime.now().day)
        text = 'วันนี้'
    elif filters_select == 'week':
        page_title = 'Report(Week)'
        order = order.filter(date_time__week=datetime.now().isocalendar()[1])
        text = 'สัปดาห์นี้'
    elif filters_select == 'month':
        page_title = 'Report(Month)'
        order = order.filter(date_time__month=datetime.now().month)
        text = 'เดือนนี้'
    elif filters_select == 'year':
        page_title = 'Report(Year)'
        order = order.filter(date_time__year=datetime.now().year)
        text = 'ปีนี้'
    for o in order:
        total += o.total_price
    context={
        'order':order,
        'total':total,
        'text':text,
        'page_title':page_title
    }
    return render(request,'report/report.html',context=context)
