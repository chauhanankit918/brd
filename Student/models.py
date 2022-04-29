import datetime
from django.db import models
from datetime import *
from Admin.models import Course
import email
from urllib import request
from django.db import models
from Student.models import Course
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime 


from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from Student.constants import PaymentStatus
from datetime import date
# Create your models here.
# def number_default_function():
#     return 'PRJ' + create_new_ref_number()
def MakeOTP():
    import random,string
    a = 'BRD/'
    b = str(''.join(random.choices( string.digits, k = 6)))
    
    
    return a+b
class Student_detail(models.Model):
    Name = models.CharField(max_length = 50 ,null=True )
    Email = models.CharField(max_length = 30 ,null=True)
    Number = models.CharField(max_length = 12 ,null=True)
    # Number2 = models.CharField(max_length = 12 ,null=True)
    DOB = models.DateField(null=True)
    
    Aadhaar = models.CharField(max_length = 12 ,null=True)
    Enrollment_date = models.DateTimeField(auto_now_add=True , null=True)
    Admission_no = models.CharField(max_length=10, default=MakeOTP())
    GENDER_CHOICES = (
        # ('NONE', 'Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    Gender = models.CharField(max_length = 6 ,null=True  ,choices=GENDER_CHOICES )
    # Father = models.CharField(max_length = 50 ,null=True)
    education = (
        ('10th','Secondary education'),
        ('12th','Senior secondary education'),
        ('Grad','Graduation education'),
        ('P.Grad','Post Graduation education'),
    )
    Education = models.CharField(max_length = 50 ,null=True,choices=education)
    Course_name = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    doc_10 =  models.FileField(upload_to='static/docs/',  null=True,blank=True)
    doc_12 =  models.FileField(upload_to='static/docs/', null=True ,blank=True)
    doc_ug =  models.FileField(upload_to='static/docs/', null=True ,blank=True)
    doc_pg =  models.FileField(upload_to='static/docs/', null=True ,blank=True)
    Address = models.TextField(max_length = 200 ,null=True)
    State = models.CharField(max_length= 20 , null=True)
    City = models.CharField(max_length = 15 , null=True)
    House = models.CharField(max_length = 15 , null=True)
    Post_office = models.CharField(max_length = 15 , null=True)
    Block = models.CharField(max_length = 15 , null=True)
    District = models.CharField(max_length = 15 , null=True)
    Pincode = models.CharField(max_length = 15 , null=True)
    # Locality = models.CharField(max_length = 15 , null=True)
    date_of_joining = models.DateField(default=datetime.today)
    paid_amount = models.BigIntegerField(default=0)
    Payment = models.BooleanField(default='False')
    Trm = models.BooleanField(default='False')
    

    def __str__(self):
        return self.Email


# payment


class Student_Payment(models.Model):
    name = models.CharField(max_length=20, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    Admission_no = models.ForeignKey(Student_detail,on_delete=models.CASCADE , null=True)
    email = models.CharField(max_length=20, null=True)
    payment_id = models.CharField(max_length = 150 , null=True)
    Razorpay_Order_Id = models.CharField(max_length=200, null=True)
    Amount = models.IntegerField( null=True)
    
    def __str__(self):
        return self.name

    # def __unicode__(self):
    #     return 

class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    Admission_no = models.ForeignKey(Student_detail,on_delete=models.CASCADE , null=True)
    
    date = models.DateField(default=date.today  )
    date2 = models.DateTimeField(default=datetime.now)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    # date = models.DateTimeField(auto_now_add=True , null=True)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.user}-{self.id}-{self.name}-{self.status}"

# payment