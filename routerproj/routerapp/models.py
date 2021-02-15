from django.db import models

class Router(models.Model):
    sapid=models.CharField(max_length=45)
    loopbackipv4=models.CharField(max_length=35)
    hostname=models.CharField(max_length=45)
    macaddress=models.CharField(max_length=64)

    
