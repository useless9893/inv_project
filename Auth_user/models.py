from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager ,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, user_name, password):
        if not user_name:
            raise ValueError('user name is required')
        if not password:
            raise ValueError('password is required')
        
        user = self.model(user_name=user_name)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, user_name,password,**kwargs):
        user = self.create_user(
            user_name ,password
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.save()
        return user



class CoreUser(AbstractBaseUser,PermissionsMixin):
        user_id = models.AutoField(primary_key=True)
        user_name = models.CharField(max_length=255,unique=True)
        first_name = models.CharField(max_length=155)
        last_name = models.CharField(max_length=155)
        email = models.EmailField(null=True,unique=True)
        contact =PhoneNumberField(null=True,unique=True)
        is_admin=models.BooleanField(default=False)
        is_staff=models.BooleanField(default=False)

        USERNAME_FIELD = 'user_name'
        REQUIRED_FIELDS = ['first_name','last_name']
        objects = UserManager() 
        class Meta:
            db_table = 'core_user'

