from email import message
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class query_form(models.Model):
    form_name = models.CharField(max_length=100,null=True)
    form_email = models.CharField(max_length=100,null=True)
    form_subject = models.CharField(max_length=100,null=True)
    form_message = models.CharField(max_length=1000,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.form_subject


class slider(models.Model):
    slider_name = models.CharField(null=True , max_length = 50 )
    slider_img = models.ImageField(upload_to='static/slider', null=True ,max_length = 100)
    Details = RichTextField(blank=True , null=True)
    
    def __str__(self):
        return self.slider_name
    
    
class q_form(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField( max_length=254 , null=True) 
    phone = models.CharField(max_length=15 , null=True)
    message = models.CharField( max_length=500, null=True)
       
       
class email_data(models.Model):
    email = models.EmailField( max_length=254 , null=True)       
    def __str__(self):
        return self.email