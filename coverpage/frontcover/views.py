from django.shortcuts import render


def bookcover(request):
    return render(request, 'frontcover/design.html')