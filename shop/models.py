from django.db import models
from django.utils.text import slugify
from accounts.models import User
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from checkout.models import BillingAddress

User = get_user_model()

CATEGORY_CHOICES = [
    #(item in db, human readable text)
    ('Jackets', 'Jackets'),
    ('Hoodies', 'Hoodies'),
    ('Tshirts', 'T-shirts'),
    ('Scarfs', 'Scarfs'),
    ('Bags', 'Bags')
]

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    #if added after initial migrations, delete the initial migration log
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
    #req: Pillow
    image = models.ImageField(upload_to='static/simplewebshop/images')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    #needed when clicking to see detail item page
    def get_absolute_url(self):
        return reverse('shop:single', kwargs={
            'slug':self.slug
        })

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    def get_final_price(self):
        if self.item.discount_price:
            return self.quantity * self.item.discount_price
        return f'{(self.quantity * self.item.price):.2f}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #will create cross reference table (join table) in db
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        BillingAddress, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def total(self):
        total = 0
        for order_item in self.items.all():
            total += float(order_item.get_final_price())
        return f'{total:.2f}'
