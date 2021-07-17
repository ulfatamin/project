from django.db.models.expressions import Value
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm




# Create your views here.
from .models import *
from .forms import *
from cart.cart import Cart
from .forms import ContactForm
#from .forms import OrderForm, CreateUserForm
#from .filters import OrderFilter

def signup(request):
    form = User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST.get['password1']
        password2 = request.POST.get['password2']
        ins=User(User_user_name=username,User_Email=email,User_password1=password1,User_password2=password2)
        ins.save()
        return redirect('/')
    return render(request, 'catering/signup.html', {'cus':form}) 
    
def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'catering/contact.html', context)    

def get_data(request):
    data=Cart.objects.all()
    context={
        'data' :data
    }
    return render(request, 'data/index.html',context)

def store(request):
    cart = Cart(request)
    ab=request.session['cart']
    print(ab)
    req.objects.create()
    max_val=req.objects.latest('id')
    print(max_val)
    for key,value in ab.items():
        print(value['name'])

        orderel.objects.create(order=max_val, name=value['name'], quan=value['quantity'], price=value['price'])

    cart.clear()

    return render(request, 'catering/index.html', {'cart': cart})

#def cart_add(request, id):
    cart = addtocart.objects.all()
    product = addtocart.objects.all()
    return redirect("index")

#def cart_add(request, id):
    cart = Cart(request)
    products = Product.objects.get(id=id)
    cart.add(product=products)
    return redirect("index")

def item_clear(request, id):
    cart = addtocart(request)
    product = addtocart.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = addtocart(request)
    product = addtocart.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = addtocart(request)
    product = addtocart.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = addtocart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'catering/cart_detail.html')

def get_page(request):
    p=product_in.objects.all()
    qs=customer.objects.all()
    return render(request, 'catering/index.html',{'pi':p,'dat':qs})

def get_page1(request):
    return render(request, 'catering/about.html')

def get_page2(request):
    return render(request, 'catering/contact.html')

def get_page3(request):
    return render(request, 'catering/signup.html')

def get_page4(request):
    return render(request, 'catering/login.html')    



def savecustomer(request):
    form = addcus()
    if request.method == 'POST':
        form = addcus(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/customers')
    context ={'form':form}
    return render(request,'catering/addcustomer.html',context)

# def showformdata(request):
#     fm= CustomerUpdation()
#     return render(request, 'catering/updation.html',{'form':fm})

def edit_data(request, pk):
    form1= customer.objects.get(id=pk)
    print(form1)
    form= addcus(instance=form1)
    if request.method == 'POST':
        form = addcus(request.POST, instance=form1)
    if form.is_valid():
        form.save()
        return redirect('/customer')
    else:
         form.errors
    context ={'form':form}
    return render(request,'catering/addcustomer.html',context)

def del_data(request, id):
    form= customer.objects.get(pk=id)
    
    form.delete()
    return redirect('/customer')

def add_to_cart(request):
    form = addtocart.objects.get()
    if request.method == 'POST':
        form = addtocart.objects.get(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/add_to_cart')
    context ={'form':form}
    return render(request,'catering/add_to_cart.html',context)

# def showformdata(request):
#     fm= CustomerUpdation()
#     return render(request, 'catering/updation.html',{'form':fm})
def show_data(request, id):
    print(id)
    form1= addtocart.objects.get(pk=id)
    print(form1)
    form= add_to_cart(instance=form1)
    if request.method == 'POST':
        form = add_to_cart(request.POST, instance=form1)
    if form.is_valid():
        form.save()
        return redirect('/add_to_cart')
    else:
         form.errors
    context ={'form':form}
    return render(request,'catering/add_to_cart.html',context)
def del_data(request, id):
    form= addtocart.objects.get(pk=id)
    
    form.delete()
    return redirect('/add_to_cart')

#def index(request):
    p = product_in.objects.all()
    add = Address.objects.all()

    return render(request,'index.html',{'product':p,'ad':add})

#def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['Username']
        email=request.POST['Email']
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        pass1=request.POST['Password']
        pass2=request.POST['Confirm Password']

        # check for errorneous input
        if (pass1!= pass2):
            return redirect('signup')
        # Create the user
        myuser = customer.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return redirect('signin')
    

    return render(request,'sign up.html')

#def update_data(request, id):
    print(id)
    form1= addtocart.objects.get(pk=id)
    print(form1)
    form= add_to_cart(instance=form1)
    if request.method == 'POST':
        form = add_to_cart(request.POST, instance=form1)
    if form.is_valid():
        form.save()
        return redirect('/add_to_cart')
    else:
         form.errors
    context ={'form':form}
    return render(request,'catering/add_to_cart.html',context)

    


def cart_add(request, id):
    cart = Cart(request)
    product = product_in.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")