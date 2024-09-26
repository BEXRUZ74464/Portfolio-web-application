from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("article", "author_full_name", "author_image", "comment")
        widgets = {
            'author_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your message'}),
        }