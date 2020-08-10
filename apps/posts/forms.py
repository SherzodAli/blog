from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    """Форма создания поста."""

    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите название статьи'}))

    class Meta:
        model = Post
        fields = ['title', 'summary', 'image']
