from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
	
	class Meta:
		model = Comment
		fields = ('name', 'email', 'description')
		labels = {
		'name': '',
		'email': '',
		'description': '',
		
		
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
			'description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Comment'}),
				
			
		}
	