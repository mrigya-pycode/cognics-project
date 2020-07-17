from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
# from django.shortcuts import render
from .models import Category,Subcategory
from django.core import serializers
# serialize queryset
# import pymysql

# class DbConnect:
#
#     def connect(self):
#         mydb = pymysql.connect(
#             host="localhost",
#             user="root",
#             passwd="root",
#             database="testlab"
#         )
#         return mydb


def index(request):
    return render(request,'cognicapp/index.html')

def datarenderstate(request):
    state = Category.objects.all()
    context = {'states': state}
    if request.method == 'POST':
        state_id = request.POST['state_select']
        city_name = request.POST['city_select']
        city_id = Subcategory.objects.get(name=city_name)
        result = str(state_id)+str(city_id.id)
        print(result)
        return HttpResponse('<h1>result is '+result+'</h1>')
    return render(request,'cognicapp/labwork.html',context)

def StatesValidate(request):
    state_id = request.GET.get('state')
    city_obj = Subcategory.objects.filter(catid = state_id)
    city_name = []
    for  i in city_obj:
        city_name.append(i.name)
    print(state_id,city_obj,city_name)
    # data = serializers.serialize('json', city_obj)
    data = {'city':city_name}
    return JsonResponse(data)


# def labwork(request):
#     mydb = DbConnect().connect()
#     mycursor = mydb.cursor()
#     sql = """select * from  cognicapp_category"""
#     mycursor.execute(sql)
#     record = mycursor.fetchall()
#     state=[]
#     for i in range(len(record)):
#         state.append(record[i][1])
#     mycursor.close()
#     mydb.close()
#     return render(request,'cognicapp/labwork.html',{'context':state})
