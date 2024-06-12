from django.db import models
from Auth_user.models import * 


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    user_id = models.ForeignKey(CoreUser,on_delete=models.CASCADE,related_name='user_client')
    company_address = models.CharField(max_length=555)
    
    def __str__(self):
        return self.client_name    
    
    class Meta:
        db_table = 'client'

class Technology_option(models.Model):
    option_id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=155)

    DisplayField = ['option_id','option']

    def __str__(self):
        return self.option
    
    class Meta:
        db_table = 'Technology_option'


class Technology(models.Model):
    tech_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    option_id = models.ForeignKey(Technology_option,on_delete=models.CASCADE,null=True)

    DisplayField = ['tech_id','name','option_id']

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Technology'
    

class Payment_method(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=55)

    DisplayField = ['payment_method_id','payment_type']

    def __str__(self):
        return self.payment_type
    
    class Meta:
        db_table = 'Payment_method'


class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(max_length=155)
    rate = models.IntegerField()

    DisplayField = ['tax_id','tax_name','rate']

    def __str__(self):
        return self.tax_name
    
    class Meta:
        db_table = 'Tax'
