from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from .models import *
# เข้าสู่ระบบ
def my_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'ชื่อผู้ใช้ หรือ รหัสผ่านผิด โปรดลองอีกครั้ง'

    return render(request,template_name='login_page.html',context=context)

# ออกจากระบบ
def my_logout(request):
    logout(request)
    return redirect('login')

# เปลี่ยนรหัสผ่าน
@login_required
def change_password(request):
    page_title = 'Change Password'
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    context={
        'form':form ,
        'page_title':page_title
        }
    return render(request,'test.html',context=context)
# หน้าหลัก
@login_required
def index(request):
    page_title = 'POSmart'
    total = 0
    search = request.GET.get('search','')
    select = request.GET.get('sel','')
    product = Product.objects.filter(name__contains=search)
    types = Type.objects.all()
    cart = My_Cart.objects.all()
    for c in cart:
        total += Product.objects.get(pk=c.products_id).price*c.amount
    if select > '0':
        product = product.filter(type=select)
    context = {
        'product':product,
        'type':types,
        'search':search,
        'select':select,
        'carts':cart,
        'total':total,
        'page_title':page_title
    }
    return render(request,'main/index.html',context=context)
# เพิ่มสินค้าในตะกร้า
def add_to_cart(request,product_id):
    product = Product.objects.get(pk=product_id)
    item = My_Cart.objects.all()
    amount = 1
    if item:
        for i in item:
            if i.products_id == product_id:
                item = My_Cart.objects.get(products_id=i.products_id)
                item.amount += 1
                break
            else:
                item = My_Cart()
                item.products_id = product_id
                item.amount = amount
    else:
        item = My_Cart()
        item.products_id = product_id
        item.amount = amount
    item.save()
    return redirect('index')
# นำสินค้าออกจากตะกร้า
def remove_to_cart(request,product_id):
    order_pro = My_Cart.objects.get(pk=product_id)
    order_pro.delete()
    return redirect('index')
# บันทึกการขาย
def order_save(request):
    total = 0
    cart = My_Cart.objects.all()
    for c in cart:
        total += Product.objects.get(pk=c.products_id).price * c.amount
    order = Order.objects.create(total_price=total)
    for c in cart:
        order_product = Order_Products.objects.create(
            order_id=order.id,
            amount=c.amount,
            product_id=Product.objects.get(pk=c.products_id).id
        )
        cart.delete()
    return redirect('index')