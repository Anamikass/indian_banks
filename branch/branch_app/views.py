from django.contrib import messages
from django.http import request
from django.shortcuts import render
from .models import bank_detail


# Create your views here.
def search_page(request):
    if request.method == 'POST':
        ifsc_code = request.POST['ifsccode']
        if bank_detail.objects.filter(bank_ifsc=ifsc_code).exists():
            branch_detail = bank_detail.objects.filter(bank_ifsc=ifsc_code).all()
            return render(request, 'search.html', {'branch_detail': branch_detail})
        else:
            messages.error(request, 'There is no such ifsc code.Please be sure to enter valid ifsc code.')
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')


def search_city(request):
    city_list = bank_detail.objects.order_by().values('bank_city').distinct()
    bank_list = bank_detail.objects.order_by().values('bank_name').distinct()
    if request.method == 'POST':
        selected_city = request.POST['city']
        selected_bank = request.POST['bank']
        branch_list = bank_detail.objects.filter(bank_name=selected_bank,bank_city=selected_city).all()
        print(branch_list)
        return render(request,'searchcity.html',{'branch_list':branch_list,'city_list':city_list,'bank_list':bank_list})
    
    
    return render(request,'searchcity.html',{'city_list':city_list,'bank_list':bank_list})
