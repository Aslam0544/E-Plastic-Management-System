from django.db import models

from django.db.models import Model

class UserModel(Model):

    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    usertype = models.CharField(max_length=50)

class WastageModel(Model):

    customerid = models.CharField(max_length=50)
    wastagename = models.CharField(max_length=50)
    image = models.FileField(upload_to="images")
    cost = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    assignedto = models.CharField(max_length=50)
    collectiondate = models.CharField(max_length=50)
    adminstatus = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True, blank=False, null=False)