import datetime
import uuid

from django.db import models
from django.db.models import SlugField
from django.utils.text import slugify


class Customer ( models.Model ) :
    customer_id = models.CharField ( max_length=5, primary_key=True )
    slug = SlugField(unique=True, blank=True, null=True)
    company_name = models.CharField ( max_length=200 )
    contact_name = models.CharField ( max_length=100, blank=True, null=True )
    contact_title = models.CharField ( max_length=100, blank=True, null=True )
    address = models.CharField ( max_length=200, blank=True, null=True )
    city = models.CharField ( max_length=100, blank=True, null=True )
    region = models.CharField ( max_length=100, blank=True, null=True )
    postal_code = models.CharField ( max_length=20, blank=True, null=True )
    country = models.CharField ( max_length=100, blank=True, null=True )
    phone = models.CharField ( max_length=50, blank=True, null=True )
    fax = models.CharField ( max_length=50, blank=True, null=True )

    def save(self, *args, **kwargs) :
        if not self.slug :
            self.slug = slugify ( self.company_name )
        super ().save ( *args, **kwargs )

    class Meta :
        db_table = 'customers'

    def __str__(self) :
        return self.company_name


class Employee ( models.Model ) :
    employee_id = models.AutoField ( primary_key=True )
    slug = SlugField(unique=True, blank=True, null=True)
    last_name = models.CharField ( max_length=100 )
    first_name = models.CharField ( max_length=100 )
    title = models.CharField ( max_length=100, blank=True, null=True )
    title_of_courtesy = models.CharField ( max_length=50, blank=True, null=True )
    birth_date = models.DateField ( blank=True, null=True )
    hire_date = models.DateField ( blank=True, null=True )
    address = models.CharField ( max_length=200, blank=True, null=True )
    city = models.CharField ( max_length=100, blank=True, null=True )
    region = models.CharField ( max_length=100, blank=True, null=True )
    postal_code = models.CharField ( max_length=20, blank=True, null=True )
    country = models.CharField ( max_length=100, blank=True, null=True )
    home_phone = models.CharField ( max_length=50, blank=True, null=True )
    extension = models.CharField ( max_length=10, blank=True, null=True )
    photo = models.ImageField ( upload_to='employees/', blank=True, null=True )
    notes = models.TextField ( blank=True, null=True )
    reports_to = models.ForeignKey (
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates'
    )
    photo_path = models.CharField ( max_length=500, blank=True, null=True )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)

    class Meta :
        db_table = 'employees'

    def __str__(self) :
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    slug = SlugField(unique=True, blank=True, null=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    order_date = models.DateField(blank=True, null=True)
    required_date = models.DateField(blank=True, null=True)
    shipped_date = models.DateField(blank=True, null=True)
    ship_name = models.CharField(max_length=200, blank=True, null=True)
    ship_address = models.CharField(max_length=200, blank=True, null=True)
    ship_city = models.CharField(max_length=100, blank=True, null=True)
    ship_region = models.CharField(max_length=100, blank=True, null=True)
    ship_postal_code = models.CharField(max_length=20, blank=True, null=True)
    ship_country = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Har safar unique slug yaratadi
            unique_id = uuid.uuid4().hex[:8]
            self.slug = f"order-{unique_id}"
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"Order #{self.order_id}"