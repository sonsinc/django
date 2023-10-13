from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app_gen.models import Product
from app_cart.models import Cart, CartItem

# Create your views here.
def create_cartId(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@login_required(login_url='/login')
def removeCart(request, product_id):
    cart = Cart.objects.get(cart_id=create_cartId(request), customer = request.user)
    product = Product.objects.get(pk=product_id)
    cartItem = CartItem.objects.get(product = product, cart = cart) #target
    cartItem.delete()
    return redirect('/cart')

@login_required(login_url='/login')
def cart(request):
    counter = 0
    total = 0
    try:
        #Retrieve shopping cart information
        cart = Cart.objects.get(cart_id = create_cartId(request), customer = request.user)
        #Retrieve item in cart information
        cartItem = CartItem.objects.filter(cart = cart)
        for item in cartItem:
            counter += item.quantity
            total += (item.product.price * item.quantity)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        cart = None
        cartItem = None
    return render(request, 'cart.html', {'cartItem':cartItem, 'total':total, 'counter':counter})

@login_required(login_url='/login')
def addCart(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    # Get or create the user's cart
    try:
        cart = Cart.objects.get(cart_id=create_cartId(request), customer=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=create_cartId(request),
            customer=request.user
        )
        cart.save()
        
    # Try to get an existing cart item for the product
    try:
        cartitem = CartItem.objects.get(product=product, cart=cart)
        if cartitem.quantity < product.stock:  # Check if quantity can be increased
            cartitem.quantity += 1
            cartitem.save()
    except CartItem.DoesNotExist:
        # If the cart item doesn't exist, create it with a quantity of 1
        if product.stock > 0:  # Check if there's available stock
            cartitem = CartItem.objects.create(
                product=product,
                cart=cart,
                quantity=1
            )
            cartitem.save()

    return redirect('/cart')
