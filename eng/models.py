from django.db import models
from django.urls import reverse
# Create your models here.



class Category(models.Model):
    parent = models.ForeignKey('self',blank=True,null=True,related_name='inside_category',on_delete=models.CASCADE)
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d')
    info = models.CharField(max_length=58, db_index=True)

    class Meta:
        ordering = ['id']
        unique_together =('slug','parent')
        verbose_name_plural = 'categories'


    def __str__(self):
        full_path = [self.name]

        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return '->'.join(full_path[::-1])



    def get_absolute_url(self):
        return reverse('engshow_category', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete = models.CASCADE)
    product_no = models.CharField(max_length=25,default='Ürün Kodu Giriniz')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    info = models.TextField(default='Ürün Aaçıklama')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    normal_price = models.CharField(max_length=4,db_index=True,default='SOME STRING')
    discount = models.CharField(max_length=4,db_index=True,default='SOME STRING')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    descrip = models.CharField(max_length=160, db_index=True, default='Description')
    keyword = models.CharField(max_length=60, db_index=True, default='Keyword')
    page_title = models.CharField(max_length=60, db_index=True, default='Sayfa Title')
    alt = models.CharField(max_length=100, db_index=True, default='Ürün İmage Alt Açıklaması')
    title = models.CharField(max_length=100, db_index=True, default='Ürün İmage Title Açıklaması')
    canocinal = models.CharField(max_length=100, db_index=True, default='https://digimaris.com/')


    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug',))

    def __str__(self):
        return self.name


    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i]='/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]



    def get_absolute_url(self):
        return reverse('engshow_category', args=[self.slug, self.id])






class BestOfWeek(models.Model):
    name = models.CharField(max_length=12, db_index=True)
    info = models.CharField(max_length=58, db_index=True)
    slug = models.SlugField(max_length=30, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=0)


    def __str__(self):
        return self.name


