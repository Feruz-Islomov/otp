from .models import Driver_cart_order
from accounts.models import CustomUser

def fetchDriverCart(request):
        driver = request.user
        # obj = Driver_cart_order.objects.filter(driver=driver)
        user = CustomUser.objects.get(id=driver.id)
        obj = user.driver_cart_order_set.all()
        return obj