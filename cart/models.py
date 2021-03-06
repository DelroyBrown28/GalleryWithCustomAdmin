from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


User = get_user_model()


class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    town_or_city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.address_1}, {self.address_2}, {self.town_or_city}, {self.postcode}"

    class Meta:
        verbose_name_plural = 'Addresses'


class SizeVariation(models.Model):
    name = models.CharField(max_length=50)
    size_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_price(self):
        return "{:.2f}".format(self.size_price / 100)


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='.')
    description = models.TextField()
    # price = models.ManyToManyField(SizeVariation)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    available_sizes = models.ManyToManyField(SizeVariation)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse("staff:product-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("staff:product-delete", kwargs={'pk': self.pk})


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(SizeVariation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    def get_raw_total_item_price(self):
        return self.quantity * self.size.size_price

    def get_total_item_price(self):
        size_price = self.get_raw_total_item_price()
        return "{:.2f}".format(size_price / 100)


class Order(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    billing_address = models.ForeignKey(
        Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)

    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"

    def get_raw_subtotal(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_raw_total_item_price()
        return total

    def get_subtotal(self):
        subtotal = self.get_raw_subtotal()
        return "{:.2f}".format(subtotal / 100)

    def get_raw_total(self):
        subtotal = self.get_raw_subtotal()
        # add tax, add delivery, subtract discounts
        # total = subtotal - discounts + tax + delivery
        return subtotal

    def get_total(self):
        total = self.get_raw_total()
        return "{:.2f}".format(total / 100)


class Payment(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=(
        ('PayPal', 'PayPal'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_product_receiver, sender=Product)

