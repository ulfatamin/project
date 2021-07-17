from django.db import models

# Create your models here.

class signin(models.Model):
    username =models.CharField(max_length=20)
    password =models.CharField(max_length=10)
    Email    =models.CharField(max_length=20)

class signup(models.Model):
    signinid = models.ForeignKey(signin,on_delete=models.CASCADE)
    username = models.CharField(max_length=20) 
    gender   = models.CharField(max_length=6)
    password = models.CharField(max_length=10)

class distributercontact (models.Model):
	username = models.CharField(max_length=20) 
	phoneno = models.CharField(max_length=15) 
	whatsappno = models.CharField(max_length=15) 
	cnic = models.CharField(max_length=13)
	city = models.CharField(max_length=20)
	email = models.CharField(max_length=20) 
	address = models.CharField(max_length=50) 

class distributerbrand (models.Model):
	brandname = models.CharField(max_length=20)

class distributorrepresentator(models.Model):
	name = models.CharField(max_length=30) 
	fathername = models.CharField(max_length=30) 
	designation = models.CharField(max_length=50) 
	phoneno = models.CharField(max_length=15) 
	cnic = models.CharField(max_length=13)
	date = models.DateField

class distributer(models.Model):
    distributercontactid = models.ForeignKey(distributercontact,on_delete=models.CASCADE)
    distributerbrandid = models.ForeignKey(distributerbrand,on_delete=models.CASCADE)

class payment(models.Model):
	accountno = models.CharField(max_length=30) 
	accountbranch = models.CharField(max_length=45) 
	amountpaid = models.IntegerField()
	paiddate = models.DateField
	paidtime = models.TimeField

class stockreceiver(models.Model):
	name = models.CharField(max_length=30) 
	phoneno = models.CharField(max_length=15) 
	whatsappno = models.CharField(max_length=15) 
	email = models.CharField(max_length=20)
	cnic = models.CharField(max_length=13) 
	address = models.CharField(max_length=50) 
	detail = models.CharField(max_length=100) 

class stockeditem(models.Model):
	itemname = models.CharField(max_length=30) 
	quantity = models.IntegerField() 
	price = models.CharField(max_length=30)

class stockorderpayment (models.Model):
	amount = models.IntegerField() 
	date = models.DateField
	time = models.TimeField
	paymentmethod = models.CharField(max_length=20) 

class stockorderdetails (models.Model):
	name = models.CharField(max_length=30) 
	quantity = models.IntegerField() 
	unitprice = models.IntegerField() 
	totalprice = models.IntegerField()
	date = models.DateTimeField

class stockorderbooking (models.Model):
    stockorderpayment   = models.ForeignKey(stockorderpayment,on_delete=models.CASCADE)
    totalbill           = models.IntegerField()
    bookingdate         = models.DateField
    bookingtime         = models.TimeField
    deliverydate        = models.DateField

class stockavailable (models.Model):
    stockorderdetails = models.ForeignKey(stockorderdetails,on_delete=models.CASCADE)
    itemname          = models.CharField(max_length=30) 
    quantity          = models.IntegerField() 
    price             = models.IntegerField()

class employeecontact (models.Model):
	name = models.CharField(max_length=30)
	phoneno = models.CharField(max_length=15)
	whatsappno = models.CharField(max_length=15)
	cnic = models.CharField(max_length=13)
	email = models.CharField(max_length=20)
	address = models.CharField(max_length=50)

class employeeincome (models.Model):
	name = models.CharField(max_length=50)
	startingdate = models.DateField
	salary = models.CharField(max_length=20)

class employeeexperience (models.Model):
	name = models.CharField(max_length=30)
	experience = models.CharField(max_length=10)
	designation = models.CharField(max_length=20)
	organization = models.CharField(max_length=20)
	joiningdate = models.DateField
	leavingdate = models.DateField
	leavingreason = models.CharField(max_length=50)

class dutytime (models.Model):
	department = models.CharField(max_length=10)
	designation = models.CharField(max_length=20)
	salary = models.IntegerField()
	bonus = models.IntegerField()
	shifts = models.CharField(max_length=2)
	dutytime = models.TimeField
	vacations = models.IntegerField()

class employeeskills (models.Model):
	skills = models.CharField(max_length=20)
	certificate = models.CharField(max_length=20)
	organization = models.CharField(max_length=10)
	yearexperience = models.CharField(max_length=10)

class chef (models.Model):
	name = models.CharField(max_length=20)
	cnic = models.CharField(max_length=13)
	phoneno = models.CharField(max_length=15)
	address = models.CharField(max_length=50)

class employee (models.Model):
    employeeexperienceid = models.ForeignKey(employeeexperience,on_delete=models.CASCADE)
    employeecontactid = models.ForeignKey(employeecontact,on_delete=models.CASCADE)
    employeeincomeid = models.ForeignKey(employeeincome,on_delete=models.CASCADE)

class customer (models.Model):
	username = models.CharField(max_length=20)
	phoneno = models.CharField(max_length=15)
	whatsappno= models.CharField(max_length=15)
	email = models.CharField(max_length=20)
	cnic = models.CharField(max_length=13)
	city = models.CharField(max_length=20,blank=True)
	address = models.CharField(max_length=50,blank=True)

class req(models.Model):
	status=models.CharField(max_length=255, default='Pending')

class order (models.Model):
    customerid = models.ForeignKey(customer,on_delete=models.CASCADE)
    ordernumber = models.IntegerField()
    totalorder = models.IntegerField()
    orderstatus = models.CharField(max_length=20)
    date = models.DateField

class orderel(models.Model):
	order = models.ForeignKey(req, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	price = models.FloatField()
	quan =models.FloatField()	

class event (models.Model):
	type = models.CharField(max_length=20)
	arrangement = models.IntegerField()
	date = models.DateField
	time = models.TimeField

class menu (models.Model):
    stockavailableid = models.ForeignKey(stockavailable,on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    perheadprice = models.IntegerField()

class booking (models.Model):
    eventid = models.ForeignKey(event,on_delete=models.CASCADE)
    menuid = models.ForeignKey(menu,on_delete=models.CASCADE)
    bookingtime = models.TimeField
    bookingdate = models.DateField
    bookingduration = models.TimeField

class arrangement (models.Model):
	totalarrangement = models.IntegerField()
	men = models.IntegerField()
	women = models.IntegerField()
	children = models.IntegerField()
    

class decoration (models.Model):
	type = models.CharField(max_length=20)
	style = models.CharField(max_length=20)
	bookingid = models.IntegerField()

class expenses (models.Model):
	name = models.CharField(max_length=30)
	amount = models.IntegerField()
	catagory = models.CharField(max_length=10)
	detail = models.CharField(max_length=30)

class financialrecord (models.Model):
    expensesid = models.ForeignKey(expenses,on_delete=models.CASCADE)
    sale = models.IntegerField()
    purchase = models.IntegerField()
    loss = models.IntegerField()
    profit = models.IntegerField()

class sell (models.Model):
    financialrecordid = models.ForeignKey(financialrecord,on_delete=models.CASCADE)
    date = models.DateField
    customerid = models.IntegerField()
    productid = models.IntegerField()

class bill (models.Model):
	customername = models.CharField(max_length=30)
	totalamount = models.CharField(max_length=20)
	billdate = models.DateField()
	billtime = models.TimeField()

class instalment (models.Model):
	firstinstalment = models.IntegerField()
	secondinstalment = models.IntegerField()
	thirdinstalment = models.IntegerField()
	remainingamount = models.IntegerField()
	date = models.DateField

class cashpayment (models.Model):
	totalamount = models.IntegerField()
	paidamount = models.IntegerField()
	paiddate = models.DateField
	paidtime = models.TimeField



class product_in(models.Model):
    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
	
class Product(models.Model):
   name = models.CharField(max_length=255) 
   image = models.ImageField(upload_to='images/') 
   price = models.FloatField()

class addtocart(models.Model):
    name = models.CharField(max_length=100) 
    quantity = models.IntegerField()
    price = models.IntegerField()

class User(models.Model):
	username = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	password1 =models.CharField(max_length=10)
	password2 =models.CharField(max_length=10)
   

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email