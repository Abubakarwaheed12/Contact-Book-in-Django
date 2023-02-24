from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def edit(request):
    return render(request, 'edit.html')

def delete(request):
    return render(request, 'delete.html')

def profile(request):
    return render(request, 'profile.html')
