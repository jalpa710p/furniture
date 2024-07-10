from django.db import models

class Menu(models.Model):
    image = models.ImageField(upload_to='Menu/')

    def __str__(self):
        return f"Menu Image: {self.image}"


class Product(models.Model):
    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (self.title)


class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.FileField(upload_to='features/', blank=True, null=True)

    def __str__(self):
        return self.title

class FeatureImage(models.Model):
    image = models.ImageField(upload_to='FeatureImage/')


class ContainerImage(models.Model):
    image = models.ImageField(upload_to='ContainerImage/')


class ItemProduct(models.Model):
    image = models.ImageField(upload_to='ItemProduct/')
    title = models.CharField(max_length=50)
    descriptions = models.TextField()


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/')
    text = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='post_images/')


class Shop(models.Model):
    image = models.ImageField(upload_to='product2/')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (self.title)


class About(models.Model):
    image = models.ImageField(upload_to='about/')


class FeatureIcon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.FileField(upload_to='featureicon/', blank=True, null=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='persons/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PostBlog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='post_blogs/')


class Contact(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phn = models.CharField(max_length=30)


class Product1(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product1/', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

   
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None


