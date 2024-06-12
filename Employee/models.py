from django.db import models
from Auth_user.models import *

class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    user_id=models.OneToOneField(CoreUser,on_delete=models.CASCADE)
    age=models.IntegerField()
    salary=models.DecimalField()
    id_proof=models.CharField(max_length=50)
    address=models.CharField(max_length=255)
    pincode=models.BigIntegerField()
    city_id=models.ForeignKey(City,on_delete=models.CASCADE)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    role_id=models.ForeignKey(Role,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id.first_name
    
    class Meta:
        db_table = 'employee'