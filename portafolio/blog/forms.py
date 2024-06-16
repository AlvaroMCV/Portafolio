from django import forms
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'required': True,
                'rows': 3, 
                'placeholder': 'Escribe tu comentario aquí',
                'style': 'resize: none; border-radius: 10px; width: 100%'
                }),
                 
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'required': True, 
                'maxlength': 100
            }),
            'contenido': forms.Textarea(attrs={
                'required': True,
                'style': 'resize: none;'
            }),
        }