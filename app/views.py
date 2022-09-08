# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the app index.")

# from attr import attributes
from django.shortcuts import render

from app.models import data, user_data
from django.db.models import Q

def index(request):
    template_name = 'index.html'
    return render(request,template_name)

def InputCreate(request):
    template_name = 'user_input.html'
    return render(request,template_name)

def player_list(request):
    template_name = 'player_list.html'
    return render(request,template_name)

def move_to_output(request):
    if request.method == 'POST':
        user_height = int(request.POST.get('Height'))
        user_weight = int(request.POST.get('Weight'))
        user_age = request.POST.get('Age')
        # Position = request.POST.get('Position')
        user_attributes = request.POST.get('Attributes')

        # params = {
        #     "Height": Height,
        #     "Weight": Weight,
        #     "Age": Age,
        #     "Position": Position,
        #     "Attributes": Attributes,
        # }
        user_position = str(request.POST.get('Position'))
    elif request.method == 'GET':
        user_height = int(request.GET.get('Height'))
        user_weight = int(request.GET.get('Weight'))
        user_age = request.GET.get('Age')
        # Position = request.GET.get('Position')
        user_attributes = request.GET.get('Attributes')

        # params = {
        #     "Height": Height,
        #     "Weight": Weight,
        #     "Age": Age,
        #     "Position": Position,
        #     "Attributes": Attributes,
        # }
        user_position = str(request.GET.get('Position'))

    user_diff_h = user_height - int(user_data.objects.all().get(age__contains=user_age).male_height)
    user_diff_w = user_weight - int(user_data.objects.all().get(age__contains=user_age).male_weight)

    user_diff_h_min = user_diff_h - 4
    user_diff_h_max = user_diff_h + 4

    user_diff_w_min = user_diff_w - 7
    user_diff_w_max = user_diff_w + 7

    def sort_value(x):
        return abs((user_diff_h - x[6]) + (user_diff_w - x[7]))

    if user_position == 'D':
        player_results_list = list(data.objects.all().filter(position__contains='D').exclude(position__contains='DM').filter(height_diff__gte=user_diff_h_min).filter(height_diff__lte=user_diff_h_max).filter(weight_diff__gte=user_diff_w_min).filter(weight_diff__lte=user_diff_w_max).filter(attributes__contains=user_attributes).values_list())
    elif user_position =='D(L)' or user_position == 'D(C)' or user_position =='D(R)':
        player_results_list = list(data.objects.all().filter(position__contains='D').filter(position__contains=user_position[-2]).exclude(position__contains='DM').filter(height_diff__gte=user_diff_h_min).filter(height_diff__lte=user_diff_h_max).filter(weight_diff__gte=user_diff_w_min).filter(weight_diff__lte=user_diff_w_max).filter(attributes__contains=user_attributes).values_list())
    elif user_position == 'M':
        player_results_list = list(data.objects.all().filter(position__contains='M').filter(height_diff__gte=user_diff_h_min).filter(height_diff__lte=user_diff_h_max).filter(weight_diff__gte=user_diff_w_min).filter(weight_diff__lte=user_diff_w_max).filter(attributes__contains=user_attributes).values_list())
    elif user_position =='M(L)' or user_position =='M(C)' or user_position =="M(R)":
            player_results_list = list(data.objects.all().filter(Q(position__contains='M') & Q(position__contains='R')).filter(height_diff__gte=user_diff_h_min).filter(height_diff__lte=user_diff_h_max).filter(weight_diff__gte=user_diff_w_min).filter(weight_diff__lte=user_diff_w_max).filter(attributes__contains=user_attributes).values_list())
    elif len(user_position)<=2:
        player_results_list = list(data.objects.all().filter(position__contains=user_position).filter(height_diff__gte=user_diff_h_min).filter(height_diff__lte=user_diff_h_max).filter(weight_diff__gte=user_diff_w_min).filter(weight_diff__lte=user_diff_w_max).filter(attributes__contains=user_attributes).values_list())
    else:
        player_results_list = list(data.objects.all().filter(position__contains=user_position[:-3]).filter(position__contains=user_position[-2]).filter(height_diff__gte=user_diff_h_min).filter(height_diff__lte=user_diff_h_max).filter(weight_diff__gte=user_diff_w_min).filter(weight_diff__lte=user_diff_w_max).filter(attributes__contains=user_attributes).values_list())


    player_results_list = list(data.objects.all().filter(position__contains=user_position).filter(height_diff__gte=user_diff_h_min).filter(height_diff__lte=user_diff_h_max).filter(weight_diff__gte=user_diff_w_min).filter(weight_diff__lte=user_diff_w_max).filter(attributes__contains=user_attributes).values_list())
    player_results_list.sort(key=sort_value)    
    result = {"result" : player_results_list} 
    return render(request, 'user_input_complete.html', result)