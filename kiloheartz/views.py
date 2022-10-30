from django.shortcuts import redirect, render, reverse
from message.models import Message
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

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
            messages.success(request, 'Your message was sent successfully')
        except:
            pass
            messages.warning(request, 'There was a problem with sending your message try again latter')

        return redirect(reverse('contact-us') + "#messages")

    return render(request, 'contact_us.html')