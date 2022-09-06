# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the app index.")

from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from .forms import InputForm
from django.urls import reverse_lazy


def index(request):
    template_name = 'index.html'
    template_text = "変数受け渡しチェック" 
    context = {"text" : template_text} 
    return render(request,template_name,context)


class InputCreateView(CreateView):
    template_name = 'user_input.html'
    form_class = InputForm
    success_url = reverse_lazy('app:user_input_complete')


class InputCreateCompleteView(TemplateView):
    template_name = 'user_input_complete.html'