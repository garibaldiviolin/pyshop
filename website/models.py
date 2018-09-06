from django.conf import settings
from django.db.models.signals import pre_save
from django.db import models
from django.urls import reverse

from .utils import unique_slug_generator


class Category(models.Model):

    description = models.CharField(max_length=50)

    def __repr__(self):
        return self.description

    def __unicode__(self):
        return self.description


class Product(models.Model):
    '''
    - The barcode length was chosen considering that usual products come with
      EAN-8, EAN-13, UPC-A or UPC-E
    - The price max length was chosen considering that the most expensive
      product in the marketplace is 999.999,999 (using 3 decimal places).
      However, this can be changed if needed
    '''

    barcode = models.CharField(primary_key=True, max_length=20)
    slug = models.SlugField(unique=True)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __repr__(self):
        return self.description

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('website:product-detail', kwargs={'slug': self.slug})


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_product_receiver, sender=Product)


class PaymentMethod(models.Model):

    description = models.CharField(unique=True, max_length=50)

    def __repr__(self):
        return self.description

    def __unicode__(self):
        return self.description


class PurchaseOrder(models.Model):

    timestamp = models.DateTimeField()
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return str(self.timestamp) + self.customer.name

    def __unicode__(self):
        return str(self.timestamp) + self.customer.name


class PurchaseItem(Product):

    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=3)
    total_price = models.DecimalField(max_digits=8, decimal_places=3)

    def __repr__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)


class PurchasePaymentMethod(models.Model):

    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.PROTECT
    )
    value = models.DecimalField(max_digits=8, decimal_places=3)

    def __repr__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)


class CartProduct(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=3)
    total_price = models.DecimalField(max_digits=8, decimal_places=3)

    def __repr__(self):
        return str(self.id) + ' - ' + self.product.title

    def __unicode__(self):
        return str(self.id) + ' - ' + self.product.title
