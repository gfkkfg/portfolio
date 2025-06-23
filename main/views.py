from django.shortcuts import render
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    all_projects = Project.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send confirmation email to your own inbox
            send_mail(
                subject=f"New Contact Message from {contact.name}",
                message=contact.message,
                from_email=contact.email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Thank you for reaching out! I'll get back to you soon.")
            form = ContactForm()  # Clear form after submission
    else:
        form = ContactForm()

    return render(request, 'main/home.html', {
        'projects': all_projects,
        'form': form,
    })
