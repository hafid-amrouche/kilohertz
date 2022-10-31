from django.shortcuts import redirect, render, reverse
from message.models import Message
from django.contrib import messages as sms


def home(request):
    return redirect('about-us')

def about_us(request):
    return render(request, 'about_us.html')

def our_services(request):
    return render(request, 'our_services.html')

def contact_us(request):
    if request.method == 'POST':
        try:
            Message.objects.create(
                email=request.POST.get('email'),
                subject=request.POST.get('subject'),
                message=request.POST.get('message'),
            )
            sms.success(request, 'Your message was sent successfully')
        except:
            pass
            sms.warning(request, 'There was a problem with sending your message try again latter')

        return redirect(reverse('contact-us') + "#messages")

    return render(request, 'contact_us.html')

def login(request):
    if request.method == 'POST':
        email_true = request.POST.get("email").lower() == "ahmedtaachout@kilohertz.com"
        password_true = request.POST.get("password") == "ahmed99@kilohertz"
        if email_true and password_true :
            request.session['is_logged'] = True 
            sms.success(request, 'You are logged in')
            return redirect('messages')
        else :
            sms.warning(request, 'Wrong cridentials')
            
    return render(request, 'login.html')

def logout(request):
    if request.session.get('is_logged'):
        request.session.pop('is_logged')
        sms.success(request, 'You are logged out')
    return redirect('login')

def messages(request):
    if request.session.get('is_logged'):
        messages = Message.objects.all().order_by("-created_date")
        return render(request, 'messages.html', {"messages_" : messages})
    else:
        return redirect('home')

