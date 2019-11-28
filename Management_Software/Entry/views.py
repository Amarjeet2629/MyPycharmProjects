from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Host, Visitor
from .forms import HostRegisterForm, VisitorRegisterForm
from django.utils import timezone
from django.shortcuts import reverse
import http.client
# Create your views here.


def HostRegister(request):
    if request.method == 'POST':
        host = HostRegisterForm(request.POST)
        if host.is_valid:
            host_form = host.save(commit=False)
            host_form.time_stamp = timezone.now()
            host_form.save()
            return HttpResponseRedirect(reverse('Entry:host_register'))
        else:
            print("Form Errors")
    else:
        host_register_form = HostRegisterForm()
        return render(request, 'host_register.html', {'host_register_form': host_register_form})


def VisitorRegister(request):
    if request.method == 'POST':
        visitor = VisitorRegisterForm(request.POST)
        if visitor.is_valid:
            visitor_form = visitor.save()
            print(visitor_form.host_name.phone_number)
            phn=visitor_form.host_name.phone_number;
            print(phn)
            otp="1234"
            conn = http.client.HTTPSConnection("api.msg91.com")

            payload = "{ \"sender\": \"SOCKET\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\": \"Message1\", \"to\": [ \"9835653102\", \"9835653102\" ] } ] }"

            headers = {
                'authkey': "241862ATXrUDrX1B5bbc4638",
                'content-type': "application/json"
            }

            conn.request("POST", "/api/v2/sendsms?country=91", payload, headers)

            res = conn.getresponse()
            data = res.read()

            print(data.decode("utf-8"))
            return HttpResponseRedirect(reverse('Entry:visitor_register'))
        else:
            print('Form Errors')
    else:
        visitor_form = VisitorRegisterForm()
        return render(request, 'visitor_register.html', {'visitor_form': visitor_form})
