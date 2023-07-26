from django import forms
from .models import Blog
from .models import Comment

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields= ["title","content","image","category"]
        labels = {
            'title': 'Titulo',
            'content': 'Contenido',
            'image': 'Imagen',
            'category': 'Categoria',
            #'status': 'Status',
        }

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)