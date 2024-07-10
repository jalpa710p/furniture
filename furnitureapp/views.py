from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FeatureImageViewSet(viewsets.ModelViewSet):
    queryset = FeatureImage.objects.all()
    serializer_class = FeatureImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ContainerImageViewSet(viewsets.ModelViewSet):
    queryset = ContainerImage.objects.all()
    serializer_class = ContainerImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ItemProductViewSet(viewsets.ModelViewSet):
    queryset = ItemProduct.objects.all()
    serializer_class = ItemProductSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FeatureIconViewSet(viewsets.ModelViewSet):
    queryset = FeatureIcon.objects.all()
    serializer_class = FeatureIconSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostBlogViewSet(viewsets.ModelViewSet):
    queryset = PostBlog.objects.all()
    serializer_class = PostBlogSerializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class Product1ViewSet(viewsets.ModelViewSet):
    queryset = Product1.objects.all()
    serializer_class = Product1Serializer
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



def about(request):
    abouts = Menu.objects.all()
    feature = Feature.objects.all()
    image = FeatureImage.objects.all()
    person = Person.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, 'about.html', context={
        'menu': abouts,
        'feature': feature,
        'image': image,
        'person': person,
        'testimonial': testimonial
    })


def blog(request):
    menu = Menu.objects.all()
    postblog = PostBlog.objects.order_by('-date')[:20]
    testimonial = Testimonial.objects.all()
    return render(request, 'blog.html', context={
        'menu': menu,
        'postblog': postblog,
        'testimonial': testimonial
    })


def addcart(request):
    if request.method == 'POST':
        name = request.POST.get('product_name')
        price = float(request.POST.get('product_price'))
        quantity = int(request.POST.get('product_quantity'))
        image = request.FILES.get('product_image')
        new_product = Product1(name=name, price=price, quantity=quantity, image=image)
        new_product.save()
        return redirect('cart')
    return render(request, 'addcart.html')
def editcart(request, id):
    product = get_object_or_404(Product1, id=id)
    if request.method == 'POST':
        product.name = request.POST.get('product_name')
        product.price = float(request.POST.get('product_price'))
        product.quantity = int(request.POST.get('product_quantity'))
        # Handle image upload
        if 'product_image' in request.FILES:
            product.image = request.FILES['product_image']

        product.save()
        return redirect('cart')

    context = {
        'product': product
    }
    return render(request, 'editcart.html', context)
def deletecart(request, id):
    product = get_object_or_404(Product1, id=id)
    product.delete()
    return redirect('cart')


def cart(request):
    product1 = Product1.objects.all()
    product_list = []
    for i in product1:
        total = i.price * i.quantity
        product_list.append({
            'id': i.id,
            'name': i.name,
            'price': i.price,
            'quantity': i.quantity,
            'total': total,
            'image_url': i.image.url if i.image else None,
        })
    return render(request, 'cart.html', context={'product1': product_list})


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    menu = Menu.objects.all()
    contacts = Contact.objects.first()
    return render(request, 'contact.html', context={
        'menu': menu,
        'contacts': contacts
    })


def index(request):
    menu = Menu.objects.all()
    product = Product.objects.all()
    features = Feature.objects.all()
    image = FeatureImage.objects.all()
    containerimages = ContainerImage.objects.all()
    itemproduct = ItemProduct.objects.all()
    testimonial = Testimonial.objects.all()
    posts = Post.objects.order_by('-date')[:3]  # Get the most recent 3 posts
    return render(request, 'index.html', context={
        'menu': menu,
        'product': product,
        'features': features,
        'image': image,
        'containerimages': containerimages,
        'itemproduct': itemproduct,
        'testimonial': testimonial,
        'posts': posts
    })


def services(request):
    menu = Menu.objects.all()
    testimonial = Testimonial.objects.all()
    product = Product.objects.all()
    feature = Feature.objects.all()
    return render(request, 'services.html', context={
        'menu': menu,
        'testimonial': testimonial,
        'product': product,
        'feature': feature
    })


def shop(request):
    shop = Shop.objects.all()
    return render(request, 'shop.html', context={
        'shop': shop
    })


def thankyou(request):
    return render(request, 'thankyou.html')
