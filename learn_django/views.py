from django.shortcuts import render,HttpResponse, get_object_or_404,redirect
from learn_django.models import Product
from learn_django.models import Visitor
from learn_django.forms import productform

# Create your views here.
# def index(request):
#     return HttpResponse("something here")
    
# def dostuff(request):
#     return HttpResponse("here")
    
# def doanything(request):
#     return HttpResponse("here I am sam")
    
# rendering template.
def index(request):
    page_name = "best page"
    return render(request,'index.html', {'name':'INDEX PAGE', 'msg':page_name,'test':'another messgage'})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    
def services(request):
    return render(request,'services.html')

def products(request):
    product_list = Product.objects.all()
    print(product_list)
    return render(request,'products.html', {'data':product_list})

def add_product(request):
    if request.method == "POST":
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = productform()
    return render(request, "add_product.html", {'form':form})
    
def edit_product(request,id):
    product_item = get_object_or_404(Product, pk=id)
    if request.method == "POST":
       form = productform(request.POST, instance = product_item)
       if form.is_valid():
          form.save()
          return redirect(products)
    else:
        form = productform(instance=product_item)
    return render (request,"add_product.html", {'form':form})
    
def visitors(request):
    visitor_list = Visitor.objects.all()
    print(visitor_list)
    return render(request,'visitors.html', {'data':visitor_list})
    
def add_visitor(request):
    if request.method == "POST":
        new_visitor = Visitor()
        new_visitor.name = request.POST.get('name')
        new_visitor.age = request.POST.get('age')
        new_visitor.email = request.POST.get('email')
        new_visitor.save()
    return render(request, "add_visitor.html")


  
    
    
    
    
