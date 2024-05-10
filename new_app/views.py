from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from new_app.models import NewModel
import json

@csrf_exempt
def mymodel_list(request):
    if request.method == 'GET':
        mymodels = NewModel.objects.all()
        data = [{'id': model.id, 'name': model.name, 'description': model.description, 'address': model.address, 'contact': model.contact, 'email': model.email, 'location': model.location} for model in mymodels]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        mymodel = NewModel.objects.create(name=data['name'], description=data['description'], address=data['address'], contact=data['contact'], email=data['email'], location=data['location'])
        return JsonResponse({'id': mymodel.id, 'name': mymodel.name, 'description': mymodel.description, 'address': mymodel.address, 'contact': mymodel.contact, 'email': mymodel.email, 'location': mymodel.location}, status=201)

@csrf_exempt
def mymodel_detail(request, pk):
    try:
        mymodel = NewModel.objects.get(pk=pk)
    except NewModel.DoesNotExist:
        return JsonResponse({'error': 'MyModel not found'}, status=404)

    if request.method == 'GET':
        data = {'id': mymodel.id, 'name': mymodel.name, 'description': mymodel.description, 'address': mymodel.address, 'contact': mymodel.contact, 'email': mymodel.email, 'location': mymodel.location}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        mymodel.name = data['name']
        mymodel.description = data['description']
        mymodel.address = data['address']
        mymodel.contact = data['contact']
        mymodel.email =  data['email']
        mymodel.location = data['location']
        mymodel.save()
        return JsonResponse({'id': mymodel.id, 'name': mymodel.name, 'description': mymodel.description, 'address': mymodel.address, 'contact': mymodel.contact, 'email': mymodel.email, 'location': mymodel.location})

    elif request.method == 'DELETE':
        mymodel.delete()
        return JsonResponse({'message': 'MyModel deleted successfully'}, status=204)

