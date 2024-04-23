from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import product, Cart, order
from django.db.models import Q
import random
import razorpay
from django.core.mail import send_mail

# Create your views here.

#  This is About 
def about(request):
    return render(request, 'about.html')



#  This is Edit 
def edit(request,rid):
    print("id to be edited: ",rid)
    return HttpResponse("id to be edited :"+rid)


def contact(request):
    return render(request, 'contact.html')


#  This is  Delete
def delete(request,rid):
    print("id to be deleted: ",rid)
    return HttpResponse("id to be edited :"+rid)




#  This is SimpleVires
class SimpleViews(View):
    def get(self,request):
        return HttpResponse("Hello From Simple View")



#   This is  Home
def home(request):
    context={}
    p=product.objects.filter(is_active=True)
    context['products']=p
    return render(request,'index.html',context)




#   This is  Product Details
def product_details(request,pid):
    p=product.objects.filter(id=pid)          
    context={}
    context['products']=p
    return render(request,'product_details.html',context)




def sliderchange(request):
    show_slider = True

    context = {
        'show_slider': show_slider,
    }
    return render(request, 'home.html', context)



#   This is Register 
def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="Fields can not be empty"
            return render(request,'register.html',context)
        elif upass !=ucpass:
            context['errmsg']="Password and Confirm Password didn't match"
            return render(request,'register.html',context)
        else:
            try:
                u=User.objects.create(password=upass,username=uname,email=uname)
                u.set_password(upass)    # Encrypted Format
                u.save()
                context['success']="user created successfully"
                return render(request,'register.html',context)
            except Exception:
                context['errmsg']="User with same username alredy Exist"
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')
    





#    Tthis is User Login
def user_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context['errmsg']="Fields can not be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)       #Start the Session
                return redirect('/home')
            else:
                context['errmsg']="Invalid username & password"
                return render(request,'login.html',context)
    else:
        return render(request,'login.html')
    



    
#   User Logout
def user_logout(request):
    logout(request)
    return redirect('/home')


#   This is nav cat path 
def catfilternav(request, category_id):
    filtered_products = product.objects.filter(cat=category_id)
    return render(request, 'index.html', {'products': filtered_products})




#   This is catfilter
def catfilter(request,cv):
    q1=Q(is_active=True)
    q2=Q(cat=cv)
    p=product.objects.filter(q1 & q2)
    context={}
    context['products']=p
    return render(request,'index.html',context)



#   This is  Add to cart
def addtocart(request,pid):
    if request.user.is_authenticated:
        userid=request.user.id
        u=User.objects.filter(id=userid)
        print(u[0])
        p=product.objects.filter(id=pid)
        print(p[0])          #project object
        q1=Q(uid=u[0])
        q2=Q(pid=p[0])
        c=Cart.objects.filter(q1 & q2)
        n=len(c)      #  [1 object]
        context={}
        context['products']=p
        if n==1:
            context['msg']="Product Alredy Exist In Cart !!"
        else:
            c=Cart.objects.create(uid=u[0],pid=p[0])
            c.save()
            context['success']="Product Added Successfully In The Cart!!"
        return render(request,'product_details.html',context)
    else:
        return redirect('/login')
    

    

#  This is Views Cart
def viewcart(request):
    if request.user.is_authenticated:
        c=Cart.objects.filter(uid=request.user.id)
        np=len(c)
        s=0
        for x in c:
            s=s+ x.pid.price * x.qty
        print(s)
        context={}
        context['products']=c
        context['total']=s
        context['n']=np
        return render(request,'cart.html',context)
    else:
        return redirect('/login')




# This is Remove
def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/viewcart')



#   This is Make Payment
def makepayment(request):
    orders = order.objects.filter(uid=request.user.id)
    total_amount = 0
    order_ids = []
    
    for order_item in orders:
        total_amount += order_item.pid.price * order_item.qty
        order_ids.append(order_item.order_id)
    
    if not order_ids:
        # Redirect if there are no orders
        return redirect('no_orders')
    
    try:
        # Create a Razorpay payment
        client = razorpay.Client(auth=("rzp_test_Jqq90822jBWYgu", "lYwQpngujkphnk9g6OG41jR1"))
        data = {"amount": total_amount * 100, "currency": "INR", "receipt": str(order_ids[0])}
        payment = client.order.create(data=data)
        
        # Pass payment data to the template
        context = {'uname': request.user.username, 'data': payment}
        return render(request, 'pay.html', context)
    
    except razorpay.errors.RazorpayError as e:
        print("Razorpay Error:", e)
        return HttpResponse("Error occurred while creating payment.")
    
    except Exception as e:
        print("Error:", e)
        return HttpResponse("Error occurred while creating payment.")



def payment_confirmation(request):
    if request.method == 'POST':
        total_amount = request.POST.get('total_amount')
        order_id = request.POST.get('order_id')
        receipt = request.POST.get('receipt')

        # Process the payment confirmation here
        # For example, update the order status to 'Paid'

        return HttpResponse("Payment Confirmed!")  # Return a success message
    else:
        return HttpResponse("Invalid Request Method")  # Handle non-POST requests



def no_orders(request):
    # Placeholder view for when there are no orders
    return HttpResponse("No orders to process payment for.")


#   This is Send mail
def sendusermail(request, uname, order_details):
    subject = "Car Management System - Order Placed Successfully"
    message = f"Dear {uname},\n\nYour order details are:\n{order_details}"

    # Corrected sender and recipient email addresses
    sender_email = "prempawar241@gmail.com"
    recipient_email = "roshanipawar456@gmail.com"

    try:
        # Send email
        send_mail(
            subject,
            message,
            sender_email,
            [recipient_email],  # List of recipient email addresses
            fail_silently=False,
        )
        return HttpResponse("Mail sent successfully")
    except Exception as e:
        # Handle any exceptions that occur during email sending
        return HttpResponse(f"Failed to send email: {str(e)}", status=500)