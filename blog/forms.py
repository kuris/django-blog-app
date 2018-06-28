#ModelForm을 상속받는 PostModelForm class
from django  import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')

