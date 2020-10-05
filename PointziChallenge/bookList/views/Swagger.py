from django.shortcuts import render


def swagger(request):
    return render(request, 'swagger.html')

