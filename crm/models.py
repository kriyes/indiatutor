from django.db import models
from django.contrib.auth.models import User
#from phone_field import PhoneField


class State(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.OneToOneField(State,on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Area(models.Model):
    city = models.OneToOneField(City,on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Job_category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Job_type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# COMPNAY TYPE ENAS IT, LIFT, REAL ESTATE 

class Company_type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# INFO WITH EVERY ONE USEr

class Common_info(models.Model):   #DJANGO/PYTHON POWER
    user = models.ForeignKey(User ,on_delete=models.CASCADE,default="")
    state = models.ForeignKey(State,on_delete=models.CASCADE,default="")
    city = models.ForeignKey(City ,on_delete=models.CASCADE,default="")
    area = models.ForeignKey(Area,on_delete=models.CASCADE,default="")
    address = models.CharField(max_length=30,default="")
    email   = models.EmailField(default="")
   # mobile  = PhoneField(blank=True, help_text='Contact phone number',default="")

    class Meta:
        abstract = True

class Key_skills(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Company(Common_info):   # use Business Listing Services
    name = models.CharField(max_length=50,default="")
    company_type = models.ForeignKey(Company_type ,on_delete=models.CASCADE,default="")
    website = models.CharField(max_length=50,default="")
    GST = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name
################# New Candidates For Job ##########################
class Job(Common_info):
    job_company_name = models.ForeignKey(Company,on_delete=models.CASCADE,default="")
    job_name = models.CharField(max_length=50)
    job_profile = models.TextField()
    job_type = models.ForeignKey(Job_type ,on_delete=models.CASCADE,default="")
    job_category = models.ForeignKey(Job_category ,on_delete=models.CASCADE,default="")
    job_salary = models.DecimalField(max_digits=10,decimal_places=2,default=10000.00)
    Job_summary = models.TextField(default="abc")
    job_responsibilities = models.TextField(default="abc")
    job_keyskills = models.ManyToManyField(Key_skills,default="COMPUTER")

    def __str__(self):
        return '%s -- Company name : %s' % (self.job_name,self.job_company_name)


class Education(models.Model):
    highest_education = models.CharField(max_length=30)
    board = models.CharField(max_length=30)

    def __str__(self):
        return '%s ' % (self.highest_education)

class Resume(Common_info):
    name_candidate = models.CharField(max_length=30)
    education = models.ManyToManyField(Education,blank=True)
    job_expriance = models.ManyToManyField(Job,blank=True)
    #extra
    date_of_birth = models.DateField()


    def __str__(self):
        return self.name
    

class Abcd(models.Model):
    name = models.CharField(max_length=20,default="test")
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    
    def __str__(self):
        return self.name , self.x*self.y + self.z
        
################# clients Type ##############################
class Wholeseller(Common_info):   # use Business Listing Services
    name = models.CharField(max_length=50,default="")
    company_type = models.ForeignKey(Company_type ,on_delete=models.CASCADE,default="")
    website = models.CharField(max_length=50,default="")
    GST = models.CharField(max_length=20,default="",)

    def __str__(self):
        return self.name

class Retailer(Common_info):   # use Business Listing Services
    name = models.CharField(max_length=50,default="")
    company_type = models.ForeignKey(Company_type ,on_delete=models.CASCADE,default="")
    website = models.CharField(max_length=50,default="")
    GST = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name

########   Business Backoffice Process  ###################

class Customer(models.Model):
    name = models.CharField(max_length=50,default="")
    email   = models.EmailField(default="")
   # mobile  = PhoneField(help_text='Contact phone number',default="")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
         return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,default="")
    price = models.FloatField()
    category = models.ManyToManyField(Category)
    details = models.TextField()
    date_created =models.DateTimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (('Pending','Pending'),
              ('Out of Delivery','Out of Delivery'),
              ('Deliverd','Deliverd'))

    # name = models.CharField(max_length=50,default="")
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_created =models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=50,null=True,choices=STATUS)


    def __str__(self):
        return self.customer.name
