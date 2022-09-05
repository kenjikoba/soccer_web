# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the app index.")

from django.shortcuts import render

from app.models import data

def index(request):
    template_name = 'index.html'
    template_text = "変数受け渡しチェック" 
    context = {"text" : template_text} 
    return render(request,template_name,context)