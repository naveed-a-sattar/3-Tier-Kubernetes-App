from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        response = requests.post('http://localhost:8000/api/business_logic/add_item/', data={'item_name': item_name})
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def remove_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        response = requests.post('http://localhost:8000/api/business_logic/remove_item/', data={'item_name': item_name})
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def update_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        new_name = request.POST.get('new_name')
        response = requests.post('http://localhost:8000/api/business_logic/update_item/', data={'item_name': item_name, 'new_name': new_name})
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Invalid request method'})
