from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin,AbstractUser
from  django.utils.translation   import gettext_lazy as _
# Create your models here.
class KarbarManager(BaseUserManager):
    '''
     custom user model manager
    '''
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise  ValueError( _("The email   must be set"))
        email=self.normalize_email(email)
        user=self.model(email=email ,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def  create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.gert('is_staff') is not True:
          raise  ValueError( _("The super_user must have is_staff True")) 
        if extra_fields.gert('is_superuser') is not True:
          raise  ValueError( _("The super_user must have is_superuser True"))  
        return  self.create_user(email,password,**extra_fields)
class  Karbar(AbstractBaseUser, PermissionsMixin):
    '''
    custom user model for  your app
    '''
    email = models.EmailField(_("email address"), unique=True)
    is_superuser =models.BooleanField(default= False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects=KarbarManager()

    def __str__(self):
        return self.email