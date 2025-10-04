from django.db import models
import datetime


# Categories of Apps
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'


# All of our Apps
class Product(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=250, default='', blank=True, null=True)
	description2 = models.CharField(max_length=250, default='', blank=True, null=True)
	description3 = models.CharField(max_length=250, default='', blank=True, null=True)
	description4 = models.CharField(max_length=250, default='', blank=True, null=True)
	image1 = models.ImageField(upload_to='uploads/product/')
	image2 = models.ImageField(upload_to='uploads/product/', blank=True, null=True)
	image3 = models.ImageField(upload_to='uploads/product/', blank=True, null=True)
	header = models.CharField(max_length=250, default='', blank=True, null=True)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	available = models.CharField(max_length=250, default='', blank=True, null=True)

	def __str__(self):
		return self.name



class Comment(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name