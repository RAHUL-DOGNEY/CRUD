from django.shortcuts import render,HttpResponseRedirect
from myapp.froms import RegistrationForm
from myapp.models import Users# Claened Data La ker save ker na ka liya Model class Kaa Object
# Create your views here.

# :This Funtion is Used for Student Data Show And Add in DataBase
def add_and_show(request):
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['pwd']
            
            reg = Users(name=nm,email=em,pwd=ps)
            reg.save()
            fm = RegistrationForm()
    else:
        fm = RegistrationForm()
    stud = Users.objects.all()
    return render(request,'myapp/show.html',{'form':fm,'st':stud})



# :This Funtion is Used for Update and Delete in DataBase
def update(request,id):
    if request.method == "POST":
        pi = Users.objects.get(pk = id)
        fm = RegistrationForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Users.objects.get(pk = id)
        fm = RegistrationForm(instance=pi)
    return render(request,'myapp/update.html',{'form':fm})




# :This Funtion is Used for Student Data Delete in DataBase
def delete_data(request,id):
    if request.method == 'POST':
        dl = Users.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')

