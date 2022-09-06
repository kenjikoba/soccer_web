# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the app index.")

from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    template_text = "変数受け渡しチェック" 
    context = {"text" : template_text} 
    return render(request,template_name,context)

def InputCreate(request):
    template_name = 'user_input.html'
    return render(request,template_name)

def move_to_output(request):
    if request.method == 'POST':
        Height = request.POST.get('Height')
        Weight = request.POST.get('Weight')
        Age = request.POST.get('Age')
        Position = request.POST.get('Position')
        Attributes= request.POST.get('Attributes')

        params = {
            "Height": Height,
            "Weight": Weight,
            "Age": Age,
            "Position": Position,
            "Attributes": Attributes,
        }
    elif request.method == 'GET':
        Height = request.GET.get('Height')
        Weight = request.GET.get('Weight')
        Age = request.GET.get('Age')
        Position = request.GET.get('Position')
        Attributes= request.GET.get('Attributes')

        params = {
            "Height": Height,
            "Weight": Weight,
            "Age": Age,
            "Position": Position,
            "Attributes": Attributes,
        }
    return render(request, 'user_input_complete.html', params)