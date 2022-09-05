# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the app index.")


from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
