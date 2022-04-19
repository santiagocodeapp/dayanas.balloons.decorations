from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'MyBalloons/index.html')


def send_email(request):
    if request.method != 'POST':
        context = {
            'fail': 'Unable to send Email...!!! Please try later.'
        }
        return render(request, 'MyBalloons/index.html', context)

    name = request.POST['Name']
    email = request.POST['Email']
    phone_number = request.POST['Phone-Number']
    subject = request.POST['Subject']
    message = request.POST['Message']

    send_mail(
        subject,
        f"{message}  From: {name}, Phone Number: {phone_number}, Email: {email}",
        email,
        ['dayan0273@hotmail.com', 'decoration.dayanas@gmail.com'],
        fail_silently=False,
    )

    context = {
        'success': 'message'
    }
    # return redirect('index', context)
    return render(request, 'MyBalloons/index.html', context)