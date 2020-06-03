from django.shortcuts import render,get_object_or_404
from .models import Category,Product,BestOfWeek
from django.core.paginator import Paginator

# Create your views here.

def engindex(request):
    category = Category.objects.all()
    best = BestOfWeek.objects.all()

    context = {
        'category': category,
        'best': best,
    }
    return render(request,'engcentral/engindex.html',context)



def engshow(request,category_slug = None):
    products = Product.objects.filter(available=True).order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 8)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

    return render(request,'engcentral/engshow.html',{'category':category,'products':products})