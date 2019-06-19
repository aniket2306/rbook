from django.shortcuts import render
from  django.contrib.auth.decorators import login_required
# Create your views here.
def home(request, *args, **kwargs):
    try: 
        print(request.GET['q'])
    except:
        pass

    
    return render(request, 'core/home.html',{})

def search(request, *args, **kwargs):
    try:
        pass
    except:
        pass
        
        
    return render(request, 'core/home.html', {})