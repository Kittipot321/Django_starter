from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return HttpResponse("หน้าจอรายการวิชาที่มีการสอนในวันนั้น ๆ ของ อ. ที่ login เข้ามา")
def two(request, course_id):
    return HttpResponse("หน้าจอรายละเอียดของแต่ละวิชา %s (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน)" % course_id)
def three(request):
    return HttpResponse("หน้าจอเช็คชื่อของแต่ละวิชาที่สามารถเช็คชื่อได้ด้วย QR code")