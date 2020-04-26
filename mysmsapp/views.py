from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from twilio.rest import Client
from django.conf import settings

# Create your views here.


def homepage(request):
    return render(request,r'mysmsapp\index.html')




def broadcast_sms(request):
    print("Send found")
    if request.method=='POST':
    
        raw_recipients=request.POST['numbers']
        recipients= raw_recipients.split(",")

        message_to_broadcast= request.POST['message']
        client= Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)

        for recipient in recipients:
            if recipient:
                client.messages.create(to=recipient,
                                    from_=settings.TWILIO_NUMBER,
                                    body=message_to_broadcast
                                      )
            else:
                return HttpResponse("<h3>The numbers are not properly formated or empty</h3>",status=200)
    return render(request,r'mysmsapp\success.html')



