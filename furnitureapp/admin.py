from django.contrib import admin
from .models import *

@admin.register(Menu)
class Menufurniture(admin.ModelAdmin):
    list_display = ['image']



@admin.register(Product)
class Productfurniture(admin.ModelAdmin):
    list_display = ['image', 'title', 'price']



@admin.register(Feature)
class FurnitureFeature(admin.ModelAdmin):
    list_display = ['title', 'description', 'icon']


@admin.register(FeatureImage)
class Imagefurniture(admin.ModelAdmin):
    list_display = ['image']


@admin.register(ContainerImage)
class ImageContainerAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(ItemProduct)
class ItemImageProduct(admin.ModelAdmin):
    list_display = ['image', 'title', 'descriptions']


@admin.register(Testimonial)
class ItemImageTestimonial(admin.ModelAdmin):
    list_display = ['name', 'position', 'image', 'text']


@admin.register(Post)
class ItemImageTestimonial(admin.ModelAdmin):
    list_display = ['title', 'author', 'date', 'image']


@admin.register(Shop)
class Shopfurniture(admin.ModelAdmin):
    list_display = ['image', 'title', 'price']


@admin.register(About)
class AboutFeature(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Person)
class PersonAbout(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position','description', 'image']


@admin.register(PostBlog)
class PostBlogTestimonial(admin.ModelAdmin):
    list_display = ['title', 'author', 'date', 'image']


@admin.register(Contact)
class Contactinfo(admin.ModelAdmin):
    list_display = ['address', 'email', 'phn']


@admin.register(Product1)
class CartInfo(admin.ModelAdmin):
    list_display = ['name','price', 'image', 'quantity']


