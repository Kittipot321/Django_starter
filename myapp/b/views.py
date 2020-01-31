from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return HttpResponse("หน้าจอ dashboard สามารถดูภาพรวมของระบบได้ว่า ในวันนั้น ๆ แต่ละวิชามีจำนวนคนเข้าเรียนกี่คน ขาดกี่คน")
def two(request):
    return HttpResponse("หน้าจอค้นหา และ export ข้อมูลการเข้าห้องเรียน ทั้งในเทอมปัจจุบัน และ ย้อนหลัง")