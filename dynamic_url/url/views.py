from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request, 'home.html') 

def page (request, myid):
     if myid == 1:
          student ={'id': myid, 'name':'tare'}
     if myid == 2: 
          student ={'id':myid, 'name': 'khanki'}
     if myid == 3:
          student ={'id': myid, 'name': 'bal'}

     return render(request, 'page.html', student)



