from .models import Car,Order
from washers.models import Driver_cart_order

def fetchAuthorCar(request):
    author = request.user
    obj = Car.objects.filter(author=author)
    return obj

def fetchAuthorOrder(request):
    customer = request.user
    orders = Order.objects.filter(customer=customer)
    carts = Driver_cart_order.objects.filter(ordered_by=str(customer.id))
    return {'orders': orders, 'carts': carts}