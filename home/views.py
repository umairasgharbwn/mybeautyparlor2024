from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contactEnquiry
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email_adress=request.POST.get('email_adress')
        phone=request.POST.get('phone')
        category=request.POST.get('category')
        date=request.POST.get('date')
        message=request.POST.get('message')
        print('name',name)
        print('email_adress',email_adress)
        print('Phone',phone )
        print('category',category)
        print('date',date)
        print('message',message)
        

        en=contactEnquiry.objects.create(name=name,email_adress=email_adress,Phone=phone,category=category,Date=date,message=message)
        en.save()
        return HttpResponse('HttpResponse')

    return render(request,"index.html")



def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name','') 
        email = request.POST.get('email_adress','')  
        phone = request.POST.get('phone','')  
        category = request.POST.get('category','') 
        date = request.POST.get('date','')
        message = request.POST.get('message','')  
        from_email = email

        en=contactEnquiry.objects.create(name=name,email_adress=email,Phone=phone,category=category,Date=date,message=message)
        en.save()
        

        html_message = f"""
            <html>
                <head></head>
                <body>
                    <h2>Portfolio Form </h2>
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Phone:</strong> {phone}</p>
                     <p><strong>Category:</strong> {category}</p>
                     <p><strong>Date:</strong> {date}</p>
                    <p><strong>Message:</strong></p>
                    <p>{message}</p>
                </body>
            </html>
        """
               
        send_mail(
            phone,
            f"Name: {name}\nEmail: {email}\n\n{message}",
            from_email,      
            ['umairasgharbwn@gmail.com'],
            fail_silently=False,
            html_message=html_message,
            )
        
      
        return HttpResponse(f"""
            <script>
                alert('Your request has been submitted. We will contact you as soon as possible.');
                window.location.href = '/';
            </script>
        """)

    return HttpResponse(f"""
        <script>
            alert('Invalid request method.');
            window.location.href = '/';
        </script>
    """)

