from django.db import models


class Product(models.Model):
    """Product model.
    """
    #: Product name
    name = models.CharField(max_length=100)

    #: Product description
    description = models.TextField(blank=True)

    #: Product Image
    image = models.ImageField(upload_to="product/images", max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name
