from django.shortcuts import (render, get_list_or_404,
                              get_object_or_404, reverse,
                              redirect)
from django.views import generic
from shop.models import Item, Order, OrderItem, CATEGORY_CHOICES
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
#settings.py INSTALLED_APPS --> add django.contrib.messages + additions to middleware

class MainPage(generic.ListView):
    #queryset = Item.objects.filter(category = 'Bags')
    model = Item
    paginate_by = 9
    template_name = 'shop/main.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        #context type --> dict
        context = super().get_context_data(**kwargs)
        for category in CATEGORY_CHOICES:
            context[category[0]] = Item.objects.filter(category = category[0]).count()
        return context

class FilteredMainPage(MainPage):
    def get_queryset(self):
        return get_list_or_404(Item, category = self.kwargs['category'])
        #return Item.objects.filter(category = self.item.category)

class ItemDetail(generic.DetailView):
    model = Item

class AddToCart(LoginRequiredMixin, generic.RedirectView):
    #mixin as 1st arguments, otherwise error
    def get_redirect_url(self, *args, **kwargs):
        return reverse('shop:main')

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, slug = self.kwargs.get('slug'))
        order_item, created = OrderItem.objects.get_or_create(
            #variable declared in class dont need self.
            item=item,
            user=self.request.user,
            ordered=False
        )
        #make sure to pass in unordered orders
        order_qs = Order.objects.filter(user=self.request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity +=1
                order_item.save()
                messages.info(self.request, 'This item quantity was updated.')
            else:
                order.items.add(order_item)
                messages.info(self.request, 'This item was added to your cart.')
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user = self.request.user, ordered_date=ordered_date)
            order.items.add(order_item)
        return super().get(request, *args, **kwargs)

class RemoveFromCart(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('shop:order-summary')

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, slug=self.kwargs.get('slug'))
        order_qs = Order.objects.filter(
            user=self.request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(item__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=self.request.user,
                    ordered=False
                )[0]
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                else:
                    order.items.remove(order_item)
        return super().get(request, *args, **kwargs)

class OrderSummaryView(LoginRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'object': order}
            return render(self.request, 'shop/order-summary.html' , context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You don't have an active order")
            #if theres no order, return user to http://127.0.0.1:8000/
            return redirect('/')
