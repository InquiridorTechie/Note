from django.shortcuts import render
import requests

def notes(request):
    response = requests.get('http://127.0.0.1:8000/api/note/')
    notes = response.json()
    length = len(notes['objects'])
    return render(request, 'api/home.html', {
        'notes' : notes['objects'],
        'len' : length
    })
