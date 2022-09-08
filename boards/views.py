from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpRequest
from django.contrib.auth.models import User
from .models import Annonce
from .forms import AnnonceForm

# Create your views here.





def homee(request):

    boards = Board.objects.all()

    return render(request,'home.html',{'boards':boards})

#def listing(request):
   # boards = Annonce.objects.all()
   # formatted_annonces = ["<li>{}</li>".format(Annonce.TypeLogement) for Annonce in boards]
  # message = """<ul>{}</ul>""".format("\n".join(formatted_annonces))
   # return HttpResponse(message)


def listing(request):

    boards = Annonce.objects.all()
    return render(request,'liste.html',{'boards':boards})

def annonce(request,annonce_id):
    
    annonce = get_object_or_404(Annonce,id=annonce_id)
    return render(request,'annonce.html',{'annonce':annonce})

def recherche(request):
    
    if request.method == "POST" :
        searched = request.POST['searched']
        annonce = Annonce.objects.filter(Title__contains=searched)
        return render(request,'recherche.html',{'searched':searched,'annonce':annonce})
    else :
        return render(request,'recherche.html')


def annonce_new(request:HttpRequest):
   
    if not request.POST:
        return  render(request,'new_annonce.html')
    else  :  
        
        annonces = Annonce(
            Title=request.POST.get('title', 'no title'),
            TypeLogement=request.POST.get('typelog' , "hi"),
            NumTel=request.POST.get('numtel'),
            NombreChambre = request.POST.get('chambre' , "1"),
            Surface=request.POST.get('surface' , "100"),
            Emplacement=request.POST.get('distance' , "100"),
            description=request.POST.get('description' , "description"),
            photo=request.FILES.get('files' , "no photo yet"),
            prix=request.POST.get('prix' , "100"),
            created_by=request.user
        )
        annonces.save()
        return render(request,'new_annonce.html')


def annonce_a_approuver(request):
   
    annoncea = Annonce.objects.all()
    
    return render(request,'annonce_a_approuver.html',{'annoncea':annoncea})


def delete_annonce(request,annonce_id):
   annonce_delete = Annonce.objects.get(id=annonce_id)     
   annonce_delete.delete()
   return redirect('/annonce/annonce_a_approuver/')


def delete_annonceapp(request,annonce_id):
   annonce_delete = Annonce.objects.get(id=annonce_id)     
   annonce_delete.delete()
   return redirect('/listing/')


    
def approuver_annonce(request,annonce_id):
   approuver_annonce = Annonce.objects.get(id=annonce_id)   
   approuver_annonce.is_approved=True  
   approuver_annonce.save(update_fields=['is_approved'])
   return redirect('/annonce/annonce_a_approuver/')


    














    


