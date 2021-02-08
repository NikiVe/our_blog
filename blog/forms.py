from .models import Post, Category
from django import forms
from form_mixin.form_mixin import BootstrapFormMixin


class PostForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


    class Meta:
        model = Post

        fields = ['title', 'content', 'category', 'post_image']
