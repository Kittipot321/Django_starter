from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Sum
from main.models import Product,Type

# การจัดการสินค้า
@login_required
def manage(request):
    page_title = 'Management'
    search = request.GET.get('search','')
    select = request.GET.get('sel','')
    product = Product.objects.filter(name__icontains=search)
    types = Type.objects.all()
    if select > '0':
        product = product.filter(type=select)
    context = {
        'product':product,
        'type':types,
        'search':search,
        'select':select,
        'page_title':page_title
    }
    return render(request,'management/manage.html',context=context)

# อัพเดทสินค้า
@login_required
def product_update(request,product_id):
    page_title = 'Update Product = %d' %product_id
    product = Product.objects.get(pk=product_id)
    type = Type.objects.all()
    notice = ''
    if request.method == 'POST':
        product.name = request.POST.get('txt_2')
        product.type_id = request.POST.get('txt')
        product.description = request.POST.get('txt_3')
        try:
            product.price = request.POST.get('txt_4')
            product.save()
            notice = 'บันทึกข้อมูลเรียบร้อยแล้ว'
        except:
            notice = 'โอ๊ะ! ประเภทข้อมูลผิดพลาด'
    context={
        'num':product_id,
        'product':product,
        'type':type,
        'notice':notice,
        'page_title':page_title
    }
    return render(request,'management/product_form.html',context=context)

# เพิ่มเข้าในตาราง product
@login_required
def add_to_database(request):
    page_title = 'Add Product'
    type = Type.objects.all()
    number = request.POST.get('txt_1')
    notice = ''
    create= ''
    try:
        create = Product.objects.create(
                type=Type.objects.get(pk=number),
                name=request.POST.get('txt_2'),
                description=request.POST.get('txt_3'),
                price=request.POST.get('txt_4'),
            )
        notice = 'การเพิ่มสินค้าของคุณสำเร็จแล้ว -> หมายเลขสินค้าที่ %s' % (create.id)
    except:
        notice = 'โอ๊ะ! ประเภทข้อมูลผิดพลาด'
    context = {
        'create':create,
        'notice':notice,
        'type':type,
        'page_title':page_title
    }
    return render(request, 'management/product_form.html', context=context)

# เพิ่มประเภทของสินค้า
@login_required
def add_type(request):
    create = Type.objects.create(name=request.POST.get('txt_typename'),
            description=request.POST.get('txt_typedesc'))
    create.save()
    return redirect('edittype')

# ลบประเภทสินค้า
@login_required
def remove_type(request,type_id):
    try:
        type = Type.objects.get(id=type_id)
        type.delete()
    except:
        return redirect(to='manage')
    return redirect(to='edittype')

# บันทึกประเภทสินค้า
@login_required
def type_update(request,type_id):
    page_title = 'Type Update'
    notice = ''
    type = Type.objects.get(pk=type_id)
    if request.method == 'POST':
        type.name = request.POST.get('name')
        type.description = request.POST.get('desc')
        type.save()
        notice = 'บันทึกสำเร็จแล้ว'
    context={
        'num':type.id,
        'type':type,
        'notice':notice,
        'page_title':page_title
    }
    return render(request,'management/type_form.html',context=context)

# หน้าเพิ่มสินค้า
@login_required
def add_product(request):
    page_title = 'Add Product'
    types = Type.objects.all()
    context = {
        'type':types,
        'page_title':page_title
    }
    return render(request,'management/product_form.html',context=context)

# ลบสินค้า
@login_required
def delete_product(request,product_id):
    products = Product.objects.get(id=product_id)
    products.delete()
    return redirect(to='manage')

# หน้าจัดการประเภทสินค้า
@login_required
def edit_type(request):
    page_title = 'Type Manage'
    type = Type.objects.all()
    context = {
        'type':type,
        'page_title':page_title
    }
    return render(request,'management/manage_type.html',context=context)
