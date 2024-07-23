from carts.models import Cart
from carts.utils import get_user_carts
from django.urls import reverse
from django.template.loader import render_to_string


class CartMixin:
    def get_cart(self, request, product=None, cart_id=None):

        if request.user.is_authenticated:
            query_kwargs = {"user": request.user}
        else:
            query_kwargs = {"session_key": request.session.session_key}
        # Для filter по продукту
        if product:
            query_kwargs["product"] = product
        # Для filter по id
        if cart_id:
            query_kwargs["id"] = cart_id

        return Cart.objects.filter(**query_kwargs).first()

    def render_cart(self, request):
        user_cart = get_user_carts(request)
        context = {"carts": user_cart}

        # if referer page is create_order add key orders: True to context
        referer = request.META.get('HTTP_REFERER')
        if reverse('orders:create_order') in referer:
            context["order"] = True

        return render_to_string(
            "carts/includes/included_cart.html", context, request=request
        )
