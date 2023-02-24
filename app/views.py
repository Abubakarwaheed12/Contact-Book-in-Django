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
    c_obj=Contact.objects.get(id=id)
    print(c_obj)
    if request.method=='POST':
        c_obj.name=request.POST.get('fullname')
        c_obj.relation_ship=request.POST.get('relationship')
        c_obj.phone=request.POST.get('ph')
        c_obj.email=request.POST.get('Email')
        c_obj.address=request.POST.get('address')
        # print(nm , rel , ph , em , addr )
        
        # c_obj(name=nm , email=em , phone=ph, relation_ship=rel , address=addr)
        c_obj.save()
        
        return redirect('home')
    
    
    context={
        'contact':c_obj,
    }
    return render(request, 'edit.html' , context)



def delete(request , id):
    c_obj=Contact.objects.get(id=id)
    c_obj.delete()
    return redirect('home')

