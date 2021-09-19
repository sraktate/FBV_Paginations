from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.core.paginator import Paginator

# Create your views here.

def Home_view(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)

def Laptop_add_view(request):
    form=LaptopModelForm()
    if request.method =='POST':
        form=LaptopModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name='laptopadd.html'
    context={'form':form}
    return render(request,template_name,context)

def Laptop_show_view(request):
    obj_list = Laptop.objects.all()
    paginator = Paginator(obj_list, 1) # Show 1 laptop per page.

    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    template_name='laptoshow.html'
    context={'page_obj':page_obj}
    return render(request,template_name,context)