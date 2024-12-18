from django import forms
from .models import Post, Comment # Import your Post model

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
    
     # Optional: Add additional custom validations
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title is too short!")
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)