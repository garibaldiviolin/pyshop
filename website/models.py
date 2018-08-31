from django.db import models


class Product(models.Model):
    '''
    - The barcode length was chosen considering that usual products come with
      EAN-8, EAN-13, UPC-A or UPC-E
    - The price max length was chosen considering that the most expensive
      product in the marketplace is 999.999,999 (using 3 decimal places).
      However, this can be changed if needed
    '''

    barcode = models.CharField(primary_key=True, max_length=20)
    title = models.TextArea()
    description = models.TextArea()
    price = models.DecimalField(max_digits=8, decimal_places=3)


# class PurchaseOrder(models.Model):
