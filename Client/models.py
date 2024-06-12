from django.db import models

# Create your models here.

class Technology_option(models.Model):
    option_id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=155)


class Technology(models.Model):
    tech_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    option_id = models.ForeignKey(Technology_option,on_delete=models.CASCADE,null=True)

class Payment_method(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=55)


class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(max_length=155)
    rate = models.IntegerField()

