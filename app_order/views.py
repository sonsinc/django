from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_cart.models import Cart, CartItem
from app_order.models import Order, OrderDetail
from app_gen.models import Product
from app_cart.views import create_cartId


# Create your views here.
login_required(login_url = '/login')
def order(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        address = request.POST['address']
        cart = Cart.objects.get(cart_id=create_cartId(request), customer=request.user)
        cartItem = CartItem.objects.filter(cart=cart)
        total = 0 
        for item in cartItem:
            total += (item.product.price * item.quantity)
        #create Purchase order
        order = Order.objects.create(
            fullname = fullname,
            phone = phone,
            address = address,
            total = total,
            customer = request.user
        )
        order.save()
        for item in cartItem:
            order_detail = OrderDetail.objects.create(
                product = item.product.name,
                quantity = item.quantity,
                price = item.product.price,
                order = order
            )
            order_detail.save()
            #Stock cut
            product = Product.objects.get(pk=item.product.id)
            product.stock = int(item.product.stock-order_detail.quantity)
            product.save()
            item.delete()
        cart.delete()
        return render(request, 'order_success.html')
    else:
        return render(request, 'order.html')

login_required(login_url = '/login')
def history(request):
    orders = Order.objects.filter(customer = request.user)
    return render(request, 'history.html', {'orders': orders})

login_required(login_url = '/login')
def orderDetail(request, order_id):
    order = Order.objects.get(pk=order_id)
    if order.customer == request.user:
        order_items = OrderDetail.objects.filter(order=order)
        return render(request, 'order_detail.html', {'order':order, 'order_items':order_items} )
    return render(request, 'order_detail.html')
