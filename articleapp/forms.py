from django import forms
from django.forms import ModelForm

from articleapp.models import Article, ArticleImage

from django.utils.translation import gettext_lazy


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article

        fields = ["title", "content"]  # writer, place는 서버 단에서 작업

        labels = {
            "title": gettext_lazy("Title"),
            "content": gettext_lazy("Comment / Memory about this place"),
        }

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title of your article"}),
            "content": forms.Textarea(attrs={"placeholder": "Write a comment or Share your memory about your place"})
        }

        error_messages = {
            "title": {
                "max_length": gettext_lazy("제목은 20자 이내로 입력해주세요.")
            }
        }


class ArticleImageForm(ModelForm):
    class Meta:
        model = ArticleImage

        fields = ["image", ]  # post(article)는 서버 단에서 작업

        labels = {
            "image": gettext_lazy("Image")
        }

