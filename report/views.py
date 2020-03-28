from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from main.models import *

# รายงานว่าจะให้ดูเป็นวัน สัปดาห์ เดือน ปี หรือทั้งหมด
@login_required
def report_filters(request,filters_select):
    order = Order.objects.all().order_by('-id')
    total = 0
    if filters_select == 'all':
        page_title = 'Report(All)'
        order = order
        text = ''
    elif filters_select == 'day':
        page_title = 'Report(Day)'
        order = order.filter(date_time__day=datetime.now().day).filter(date_time__year=datetime.now().year)
        text = 'วันนี้'
    elif filters_select == 'week':
        page_title = 'Report(Week)'
        order = order.filter(date_time__week=datetime.now().isocalendar()[1]).filter(date_time__year=datetime.now().year)
        text = 'สัปดาห์นี้'
    elif filters_select == 'month':
        page_title = 'Report(Month)'
        order = order.filter(date_time__month=datetime.now().month).filter(date_time__year=datetime.now().year)
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
