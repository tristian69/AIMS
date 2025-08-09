from django.shortcuts import render

# Create your views here.
def submit(request):
    return render(request, 'aims/submit.html')  # 템플릿이 없으면 오류 발생 주의