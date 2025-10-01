from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def submission_view(request):
#     return HttpResponse("submission page (stub)")
def submission(request):
    return render(request, 'manuscripts/submission.html')

def ai_reviewer_view(request):
    return HttpResponse("ai reviewer (stub)")

def editorial_view(request):
    return HttpResponse("editorial (stub)")

def publication_view(request):
    return HttpResponse("publication (stub)")

def dashboard_view(request):
    return HttpResponse("dashboard (stub)")

# --- 아래 3개 추가 (urls.py에 맞추기) ---
def gallery_view(request):
    return HttpResponse("gallery (stub)")

def history_view(request):
    return HttpResponse("history (stub)")

def news_view(request):
    return HttpResponse("news (stub)")