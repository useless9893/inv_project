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