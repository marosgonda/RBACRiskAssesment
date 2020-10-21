from django.db import models

class MidPointObjectType(models.Model):
    id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=50)
    rest_name = models.CharField(max_length=50)
    common_name = models.CharField(max_length=50)

class Resource(models.Model):
    oid = models.CharField(primary_key=True, max_length =50)
    version = models.IntegerField()
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    objectType = models.ForeignKey(MidPointObjectType,on_delete=models.CASCADE)