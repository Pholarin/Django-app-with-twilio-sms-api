from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from twilio.rest import Client
from django.conf import settings
import openpyxl

# Create your views here.


def homepage(request):
    return render(request,r'mysmsapp\index.html')




def broadcast_sms(request):

    if request.method=='POST':
    
        excel_recipients=request.FILES['numbers']
        try:
            wb = openpyxl.load_workbook(excel_recipients)
        except Exception:
             return render(request,r'mysmsapp\index.html',{"error":"Invalid File Type"})

        worksheet =wb['Sheet1']
        number_inExcel=list()

        for row in worksheet.iter_rows():
            for cell in row:
                number_inExcel.append(cell.value)


        message_to_broadcast = request.POST['message']
        client= Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)

        for recipient in number_inExcel:
            if recipient:
                client.messages.create(to=recipient,
                                    from_=settings.TWILIO_NUMBER,
                                    body=message_to_broadcast
                                      )
            else:
                return render(request,r'mysmsapp\index.html',{"error":"Invalid Numbers"})
        return render(request,r'mysmsapp\success.html')

    return render(request,r'mysmsapp\index.html')

