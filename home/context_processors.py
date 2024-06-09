
from .models import CartItem,ProductVariation
def items_count(requset):
   if requset.user.is_authenticated:
      a = CartItem.objects.filter(user=requset.user).count()
      message = ("شحن مجاني لاي اوردر فوق ال 1000")
      cart_items = CartItem.objects.filter(user=requset.user)
      total_price = sum(item.ProductVariation.discount * item.quantity for item in cart_items)
      offer = round(1000-total_price)
      if total_price > 1:
         offer = round(1000-total_price)
         message = ("فاضلك "+(str(offer))+" عشان العرض يكمل")
      if total_price >= 1000 :
         message = ("دلوقتي ليك شحن مجاني")
      else :
            message = ("شحن مجاني لاي اوردر فوق ال 1000")
      return {'items_count':a,'offer':message}
   else:
       device = requset.COOKIES['device']
       a = CartItem.objects.filter(device=device).count()
       message = ("شحن مجاني لاي اوردر فوق ال 1000")
       cart_items = CartItem.objects.filter(device=device)
       total_price = sum(item.ProductVariation.discount * item.quantity for item in cart_items)
       offer = round(1000-total_price)
       if total_price > 1:
         offer = round(1000-total_price)
         message = ("فاضلك "+(str(offer))+" عشان العرض يكمل")
       if total_price >= 1000 :
         message = ("دلوقتي ليك شحن مجاني")
       else :
            message = ("شحن مجاني لاي اوردر فوق ال 1000")
       return {'items_count':a,'offer':message}

