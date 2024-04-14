from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    adress = models.TextField(max_length=500)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Client_name: {self.name};\n'
                f'email: {self.email};\n'
                f'phone: {self.phone};\n'
                f'adress: {self.adress};\n'
                f'registration_date: {self.registration_date}')


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def __str__(self):
        return (f'Product name: {self.name};\n'
                f'Description: {self.description};\n'
                f'Price: {self.price};\n'
                f'Count: {self.count}')

    def get_summary(self):
        words = self.description.split()
        return f'{" ".join(words[:12])}...'



class Order(models.Model):
    products = models.ManyToManyField(Product)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'ID: {self.pk};\n'
                f'Total Price: {self.total_price};\n'
                f'Date: {self.order_date}')


class Category(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product)
