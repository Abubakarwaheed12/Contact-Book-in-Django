from django.shortcuts import render
from app.models import Contact
# Create your views here.
def home(request):
    allcontact=Contact.objects.all()
    print(allcontact)
    q=request.GET.get('name')
    if q:
        allcontact=Contact.objects.filter(name__contains=request.GET.get('name'))
    if q==None:
        q=''
    context={
        'contacts':allcontact,
    }
    return render(request, 'index.html' , context)


def edit(request):
    return render(request, 'edit.html')

def delete(request):
    return render(request, 'delete.html')

def profile(request):
    return render(request, 'profile.html')
