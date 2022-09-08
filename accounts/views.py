
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from .models import Account,Question
from boards.models import Annonce
from django.shortcuts import render, get_object_or_404,redirect , HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def askQuestion(request):
       if not request.POST:
            return  render(request,'question.html')
       else  :  
            question = Question(
                Question=request.POST.get('question', 'no question'),
                created_by=request.user
            )
            question.save()
            return render(request,'question.html')



def reponsequestion(request):
    
    if request.POST:
        question = Question.objects.get(id=request.POST["question"])
        question.Reponse=request.POST.get('reponse','no reponse')
        question.is_responded=True
        question.save(update_fields=['Reponse','is_responded'])
        return redirect('/reponsequestion') 
    else:
        questions=Question.objects.filter(is_responded=False)
        return render(request,'reponsequestion.html',{'questions':questions})

def reponse(request):
    questions=Question.objects.filter(created_by_id=request.user.id)
    return render(request,'reponse.html',{'questions':questions})



   

def annonceprof(request,annonce_id):
    
    annonce = get_object_or_404(Annonce,id=annonce_id)
    return render(request,'annonceprof.html',{'annonce':annonce})

def delete_annonceprof(request,annonce_id):
    
    if request.POST.get("delete"):
        annonce_delete = Annonce.objects.get(id=request.POST["delete"])    
        annonce_delete.delete()
        return redirect('/profile/annonces')
    else : 
        annonce_delete = Annonce.objects.get(id=annonce_id)    
        annonce_delete.delete()
        return redirect('/profile/annonces')

def edit_annonce(request,annonce_id):
    annonce=Annonce.objects.get(id=annonce_id)    
    if request.POST.get("bouton"):
          return render(request,'editannonce.html',{'annonce':annonce})
    elif request.POST:
        annonce = get_object_or_404(Annonce,id=annonce_id)
        if request.POST.get('title'):
            annonce.Title=request.POST.get('title')
        if request.POST.get('typelog'):
            annonce.TypeLogement=request.POST.get('typelog')
        if request.POST.get('chambre'):    
            annonce.NombreChambre=request.POST.get('chambre')
        if request.POST.get('surface'):    
            annonce.Surface=request.POST.get('surface')
        if request.POST.get('distance'):    
            annonce.Emplacement=request.POST.get('distance')   
        if request.POST.get('description'):    
            annonce.description=request.POST.get('description')
        if request.FILES.get('photo'):    
            annonce.photo=request.FILES.get('photo')    
        if request.POST.get('numtel'):    
            annonce.NumTel=request.POST.get('numtel') 
        if request.POST.get('prix'):     
            prix=request.POST.get('prix'),   
            
        annonce.save(update_fields=['Title','TypeLogement','NombreChambre','Surface','Emplacement','description','photo','NumTel','prix'])
        return redirect('/profile/annonces') 
    else:
        return render(request,'editannonce.html')



def home(request):
    return render(request,'index.html')


def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            account = form.save()
            auth_login(request,account)
            return redirect('home')

    return render(request,'signup.html',{'form':form})

def profile(request):
    
    account=get_object_or_404(Account,id=request.user.id)
   
    
    return render(request,'profile.html',{'account':account})


def profile_annonces(request):
    account=get_object_or_404(Account,id=request.user.id)
    annonces=Annonce.objects.filter(created_by_id=request.user.id)
    if not annonces:
        annonces = []

    return render(request,'profile_annonces.html',{'annonces':annonces,'account':account})


def profile_edit(request):
    account=get_object_or_404(Account,id=request.user.id)
    if request.POST:
        if request.POST.get('username'):
            account.username=request.POST.get('username')
        if request.POST.get('firstname'):
            account.first_name=request.POST.get('firstname')
        if request.POST.get('lastname'):    
            account.last_name=request.POST.get('lastname')
        if request.POST.get('email'):    
            account.email=request.POST.get('email')
        if request.FILES.get('photoprofile'):    
            account.Profilephoto=request.FILES.get('photoprofile')   
        if request.POST.get('phonenum'):    
            account.PhoneNumber=request.POST.get('phonenum')
            
        account.save(update_fields=['username','first_name','last_name','email','Profilephoto','PhoneNumber'])
        return redirect('/profile') 
    else:
        return render(request,'profile_edit.html',{'account':account})

def enetcom(request):
    return render(request,'enetcom.html')
def isims(request):
    return render(request,'isims.html')
def isgi(request):
    return render(request,'isgi.html')
def isms(request):
    return render(request,'isms.html')
def foyersetatique(request):
    return render(request,'foyersetatique.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def base(request):
    return render(request,'base.html')
def nouvelleannonce(request):
    return render(request,'nouvelleannonce.html')
def clubs(request):
    return render(request,'clubs.html')
def cafés(request):
    return render(request,'cafés.html')
def restaurants(request):
    return render(request,'restaurant.html')
def mosquées(request):
    return render(request,'mosquées.html')
def supermarchés(request):
    return render(request,'supermarchés.html')
def centre(request):
    return render(request,'centrecommercial.html')
def clubenetcom(request):
    return render(request,'clubenetcom.html')
def manifestation(request):
    return render(request,'manifestation.html')    
def bib(request):
    return render(request,'bib.html')
  



