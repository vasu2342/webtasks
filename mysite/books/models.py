from __future__ import unicode_literals

from django.db import models


class Router(models.Model):
    # HARDCOVER = 1
    # PAPERBACK = 2
    # EBOOK = 3
    # BOOK_TYPES = (
    #     (HARDCOVER, 'Hardcover'),
    #     (PAPERBACK, 'Paperback'),
    #     (EBOOK, 'E-book'),
    # )
    sapid = models.CharField(max_length=50)
    ipv4=models.GenericIPAddressField()
    macaddress= models.CharField(max_length=30, blank=True)
    loopbackipv4= models.GenericIPAddressField()