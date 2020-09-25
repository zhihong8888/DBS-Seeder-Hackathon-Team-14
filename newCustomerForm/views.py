import requests
from django.shortcuts import render


def index(request):
    return render(request, "newCustomerForm.html")


def newCustomerFormVerification(request):
    if request.method == 'POST':
        customerForm = JSONParser().parse(request)
        print(customerForm)
        # response = requests.post("http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/validateForm",customerForm)
