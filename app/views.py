from django.shortcuts import render , redirect
from app.models import Contact
# Create your views here.
def home(request):
    allcontact=Contact.objects.all()
    q=request.GET.get('name')
    if q:
        allcontact=Contact.objects.filter(name__contains=request.GET.get('name'))
    if q==None:
        q=''
    context={
        'contacts':allcontact,
    }
    return render(request, 'index.html' , context)


# Add Contact
def add(request):
    if request.method=='POST':
        nm=request.POST.get('fullname')
        rel=request.POST.get('relationship')
        ph=request.POST.get('phonenumber')
        em=request.POST.get('email')
        addr=request.POST.get('address')
        # print(nm , rel , ph , em , addr )
        Contact.objects.create(name=nm , relation_ship=rel , phone=ph , email=em , address=addr)
        
        return redirect('home')
    return render(request, 'add.html')


def profile(request , id):
    c_obj=Contact.objects.get(pk=id)
    # print(c_obj)
    context={
        'contact':c_obj,
    }
    return render(request, 'profile.html' , context)


def edit(request , id):
    c_obj=Contact.objects.get(pk=id)
    if request.method=='POST':
        nm=request.POST.get('fullname')
        rel=request.POST.get('relationship')
        ph=request.POST.get('ph')
        em=request.POST.get('Email')
        addr=request.POST.get('address')
        print(nm , rel , ph , em , addr )
        c=Contact(name=nm , email=em , phone=ph, relation_ship=rel , address=addr)
        c.save()
        
        return redirect('home')
    
    
    context={
        'contact':c_obj,
    }
    return render(request, 'edit.html' , context)



def delete(request):
    return render(request, 'delete.html')


