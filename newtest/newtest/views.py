from django.shortcuts import render


def home(request):
    render(request, 'base_layout.html')
