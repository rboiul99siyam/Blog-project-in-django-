from django import forms

from posts.models import Post

class Add_post(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['Author']
        widgets = {
        'catagroy': forms.CheckboxSelectMultiple(attrs={'type': 'select'})
}
