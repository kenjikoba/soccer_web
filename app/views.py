# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the app index.")

from attr import attributes
from django.shortcuts import render

from app.models import data, user_data

# TODO: ユーザ入力の変数と対応
user_age = 20
user_height = 170
user_position = 'DM'
user_attributes = 'Control'
user_diff = 0 # TODO: user_ageで場合分け
user_diff_min = user_diff - 5
user_diff_max = user_diff + 5

def index(request):
    template_name = 'index.html'
    player_results_list = list(data.objects.all().filter(position__contains=user_position).filter(height_diff__gte=user_diff_min).filter(height_diff__lte=user_diff_max).values_list())
    player_results = list(data.objects.all().filter(position__contains=user_position).filter(height_diff__gte=user_diff_min).filter(height_diff__lte=user_diff_max))
    player_head = player_results[0].full_name
    player = player_results_list
    # Toni Kroosと表示される
    context = {"result" : player} 
    return render(request,template_name,context)

def InputCreate(request):
    template_name = 'user_input.html'
    return render(request,template_name)

def player_list(request):
    template_name = 'player_list.html'
    return render(request,template_name)

def move_to_output(request):
    if request.method == 'POST':
        user_height = int(request.POST.get('Height'))
        # Weight = request.POST.get('Weight')
        user_age = int(request.POST.get('Age'))
        # Position = request.POST.get('Position')
        user_attributes = request.POST.get('Attributes')

        # params = {
        #     "Height": Height,
        #     "Weight": Weight,
        #     "Age": Age,
        #     "Position": Position,
        #     "Attributes": Attributes,
        # }
        user_position = request.POST.get('Position')
    elif request.method == 'GET':
        user_height = int(request.GET.get('Height'))
        # Weight = request.GET.get('Weight')
        user_age = int(request.GET.get('Age'))
        # Position = request.GET.get('Position')
        user_attributes = request.GET.get('Attributes')

        # params = {
        #     "Height": Height,
        #     "Weight": Weight,
        #     "Age": Age,
        #     "Position": Position,
        #     "Attributes": Attributes,
        # }
        user_position = request.GET.get('Position')
    # 入力をPositionだけDMとかなんかって入力したら検索できる。
    # player_results_list = list(data.objects.all().filter(position__contains=user_position).values_list())
    user_diff = user_height - int(user_data.objects.all().get(age__contains=user_age).male_height)
    user_diff_min = user_diff - 5
    user_diff_max = user_diff + 5
    player_results_list = list(data.objects.all().filter(position__contains=user_position).filter(height_diff__gte=user_diff_min).filter(height_diff__lte=user_diff_max).filter(attributes__contains=user_attributes).values_list())
    result = {"result" : player_results_list} 
    return render(request, 'user_input_complete.html', result)

    # .filter(attributes__contains=user_attributes)