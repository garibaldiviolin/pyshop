""" website models """

from django.conf import settings
from django.db.models.signals import pre_save
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy

from .utils import unique_slug_generator


class Category(models.Model):
    """ Categories of products """

    description = models.CharField(
        max_length=50, verbose_name=ugettext_lazy('Description')
    )

    class Meta:
        """ Category's Meta class """

        verbose_name = ugettext_lazy('Category')
        verbose_name_plural = ugettext_lazy('Categories')

    def __repr__(self):
        return self.description

    def __str__(self):
        return self.description


class ProductBase(models.Model):
    """ Class that represents a abstraction for both Product and PurchaseItem.
    It contains common fields between the two models """

    barcode = models.CharField(
        primary_key=True, max_length=20,
        verbose_name=ugettext_lazy('Barcode')
    )
    title = models.TextField(verbose_name=ugettext_lazy('Title'))
    description = models.TextField(verbose_name=ugettext_lazy('Description'))
    image = models.ImageField(verbose_name=ugettext_lazy('Image'))
    price = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name=ugettext_lazy('Price')
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name=ugettext_lazy('Category')
    )

    class Meta:
        """ ProductBase's Meta class """

        abstract = True

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Product(ProductBase):
    '''
    - The barcode length was chosen considering that usual products come with
      EAN-8, EAN-13, UPC-A or UPC-E
    - The price max length was chosen considering that the most expensive
      product in the marketplace is 999.999,999 (using 3 decimal places).
      However, this can be changed if needed
    '''

    class Meta:
        """ Product's Meta class """

        verbose_name = ugettext_lazy('Product')
        verbose_name_plural = ugettext_lazy('Products')

    barcode = models.CharField(
        primary_key=True, max_length=20, verbose_name=ugettext_lazy('Barcode')
    )
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('website:product-detail', kwargs={'slug': self.slug})


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_product_receiver, sender=Product)


class PaymentMethod(models.Model):
    """ The possible methods of payments for the new purchase orders """

    description = models.CharField(
        unique=True, max_length=50, verbose_name=ugettext_lazy('Description')
    )

    class Meta:
        """ PaymentMethod's Meta class """

        verbose_name = ugettext_lazy('PaymentMethod')
        verbose_name_plural = ugettext_lazy('PaymentMethods')

    def __repr__(self):
        return self.description

    def __str__(self):
        return self.description


class PurchaseOrder(models.Model):
    """ The acquisition's header fields """

    timestamp = models.DateTimeField(verbose_name=ugettext_lazy('Timestamp'))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=ugettext_lazy('User')
    )
    cart = models.BooleanField(verbose_name=ugettext_lazy('Cart'))

    class Meta:
        """ PurchaseOrder's Meta class """

        verbose_name = ugettext_lazy('PurchaseOrder')
        verbose_name_plural = ugettext_lazy('PurchaseOrders')

    def __repr__(self):
        return '{} - {}'.format(str(self.id), self.user.username)

    def __str__(self):
        return '{} - {}'.format(str(self.id), self.user.username)


class PurchaseItem(ProductBase):
    """ The products of a specific PurchaseOrder """

    id = models.AutoField(primary_key=True)
    barcode = models.CharField(
        max_length=20, verbose_name=ugettext_lazy('Barcode')
    )
    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE,
        verbose_name=ugettext_lazy('PurchaseOrder')
    )
    quantity = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name=ugettext_lazy('Quantity')
    )
    total_price = models.DecimalField(
        max_digits=8, decimal_places=3,
        verbose_name=ugettext_lazy('TotalPrice')
    )
    slug = None  # this class doesn't use this attribute

    class Meta:
        """ PurchaseItem's Meta class """

        verbose_name = ugettext_lazy('PurchaseItem')
        verbose_name_plural = ugettext_lazy('PurchaseItems')

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class PurchasePaymentMethod(models.Model):
    """ The payment methods chosen by the user/customer for a specific
    purchase order
    """

    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE,
        verbose_name=ugettext_lazy('PurchaseOrder')
    )
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.PROTECT,
        verbose_name=ugettext_lazy('PaymentMethod')
    )
    value = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name=ugettext_lazy('Value')
    )

    class Meta:
        """ PurchasePaymentMethod's Meta class """

        verbose_name = ugettext_lazy('PurchasePaymentMethod')
        verbose_name_plural = ugettext_lazy('PurchasePaymentMethods')

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)
