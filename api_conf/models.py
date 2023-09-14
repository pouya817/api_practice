from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

# Create your models here.
class usermaneger(BaseUserManager):
    

    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('user should have email adress')
        email=self.normalize_email(email)
        user=self.model(email=email , name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self , email ,name , password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user




class userprofile(AbstractBaseUser,PermissionsMixin):
    """
    create user in my system
    """
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = usermaneger()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """ get user full name"""
        return self.name

    def get_name(self):
        """ get user name"""
        return self.name
    
    def __str__(self):
        """convert object to string"""
        return self.email
