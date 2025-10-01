from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def submission_view(request):
#     return HttpResponse("submission page (stub)")
def products(request):
    return render(request, 'products/products.html')