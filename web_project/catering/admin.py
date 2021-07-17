from django.contrib import admin
from .models import *
# Register your models here.

class cdistributercontact(admin.ModelAdmin):
    list_display=['id','username','phoneno','whatsappno','cnic','city','email','address']
class cdistributerbrand(admin.ModelAdmin):
    list_display=['id', 'brandname']
class cdistributorrepresentator(admin.ModelAdmin):
    list_display=['id', 'name','fathername','designation','phoneno','cnic','date']
class cdistributer(admin.ModelAdmin):
    list_display=['id', 'distributercontactid','distributerbrandid']
class cpayment(admin.ModelAdmin):
    list_display=['id','accountno','accountbranch','amountpaid','paiddate','paidtime']
class cstockreceiver(admin.ModelAdmin):
    list_display=['id','name','phoneno','whatsappno','email','cnic','address','detail']
class cstockeditem(admin.ModelAdmin):
    list_display=['id','itemname','quantity','price']
class cstockorderpayment(admin.ModelAdmin):
    list_display=['id','amount','date','time','paymentmethod']
class cstockorderdetails(admin.ModelAdmin):
    list_display=['id','name','quantity','unitprice','totalprice','date']
class cstockorderbooking(admin.ModelAdmin):
    list_display=['id','stockorderpayment','totalbill','bookingdate','bookingtime', 'deliverydate']
class cstockavailable(admin.ModelAdmin):
    list_display=['id','stockorderdetails','itemname','quantity','price']
class cemployeecontact(admin.ModelAdmin):
    list_display=['id','name','phoneno','whatsappno','cnic','email','address']
class cemployeeincome(admin.ModelAdmin):
    list_display=['id','name','startingdate','salary']
class cemployeeexperience(admin.ModelAdmin):
    list_display=['id','name','experience','designation','organization','joiningdate','leavingdate','leavingreason']
class cdutytime(admin.ModelAdmin):
    list_display=['id','department','designation','salary','bonus','shifts','dutytime','vacations']
class cemployeeskills(admin.ModelAdmin):
    list_display=['id','skills','certificate','organization','yearexperience']
class cchef(admin.ModelAdmin):
    list_display=['id','name','cnic','phoneno','address']
class cemployee(admin.ModelAdmin):
    list_display=['id','employeeexperienceid','employeecontactid','employeeincomeid']
class ccustomer(admin.ModelAdmin):
    list_display=['id','username','phoneno','whatsappno','email','cnic','city','address']
class corder(admin.ModelAdmin):
    list_display=['id','customerid','ordernumber','totalorder','orderstatus','date']
class cevent(admin.ModelAdmin):
    list_display=['id','type','arrangement','date','time']
class cmenu(admin.ModelAdmin):
    list_display=['id','stockavailableid','type','perheadprice']
class cbooking(admin.ModelAdmin):
    list_display=['id','eventid','menuid','bookingtime','bookingdate','bookingduration']
class carrangement(admin.ModelAdmin):
    list_display=['id','totalarrangement','men','women','children']
class cdecoration(admin.ModelAdmin):
    list_display=['id','type','style','bookingid']
class cexpenses(admin.ModelAdmin):
    list_display=['id','name','amount','catagory','detail']
class cfinancialrecord(admin.ModelAdmin):
    list_display=['id','expensesid','sale','purchase','loss','profit']
class csell(admin.ModelAdmin):
    list_display=['id','financialrecordid','date','customerid','productid']
class cbill(admin.ModelAdmin):
    list_display=['id','customername','totalamount','billdate','billtime']
class cinstalment(admin.ModelAdmin):
    list_display=['id','firstinstalment','secondinstalment','thirdinstalment','remainingamount','date']
class ccashpayment(admin.ModelAdmin):
    list_display=['id','totalamount','paidamount','paiddate','paidtime']

admin.site.register(distributercontact,cdistributercontact)
admin.site.register(distributerbrand,cdistributerbrand)
admin.site.register(distributorrepresentator,cdistributorrepresentator)
admin.site.register(distributer,cdistributer)
admin.site.register(payment,cpayment)
admin.site.register(stockreceiver,cstockreceiver)
admin.site.register(stockeditem,cstockeditem)
admin.site.register(stockorderpayment,cstockorderpayment)
admin.site.register(stockorderdetails,cstockorderdetails)
admin.site.register(stockorderbooking,cstockorderbooking)
admin.site.register(stockavailable,cstockavailable)
admin.site.register(employeecontact,cemployeecontact)
admin.site.register(employeeincome,cemployeeincome)
admin.site.register(employeeexperience,cemployeeexperience)
admin.site.register(dutytime,cdutytime)
admin.site.register(employeeskills,cemployeeskills)
admin.site.register(chef,cchef)
admin.site.register(employee,cemployee)
admin.site.register(customer,ccustomer)
admin.site.register(order,corder)
admin.site.register(event,cevent)
admin.site.register(menu,cmenu)
admin.site.register(booking,cbooking)
admin.site.register(arrangement,carrangement)
admin.site.register(decoration,cdecoration)
admin.site.register(expenses,cexpenses)
admin.site.register(financialrecord,cfinancialrecord)
admin.site.register(sell,csell)
admin.site.register(bill,cbill)
admin.site.register(instalment,cinstalment)
admin.site.register(cashpayment,ccashpayment)
admin.site.register(product_in)
#admin.site.register(Product)
admin.site.register(signup)
#Sadmin.site.register(addtocart)
admin.site.register(User)
admin.site.register(orderel)
#admin.site.register(req)

class OderItemInline(admin.TabularInline):
    model = orderel
    raw_id_fields = ['order']

@admin.register(req)
class OrderAdmin(admin.ModelAdmin):
    List_display = ['id']
    inlines = [OderItemInline]
