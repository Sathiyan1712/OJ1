from django.shortcuts import render

# Create your views here.
# Create your views here.
def home(request):
    return render(request,'home.html')

def choose_action(request):
    action=request.GET.get('action')
    context={
        'action':action,
    }
    return render(request, 'choose_action.html',context)

def Register_teach(request):
    return 0
def Register_stud(request):
    return 0

def Login_teach(request):
    return 0
def Login_stud(request):
    return 0
