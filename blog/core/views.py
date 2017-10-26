from blog.core.forms import ContactForm
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context


def home(request):
    return render(request, 'index.html')


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get(
                'name'
                , '')
            contact_email = request.POST.get(
                'email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'name': name,
                'email': contact_email,
                'content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })


def about(request):
    return render(request, 'about.html')
