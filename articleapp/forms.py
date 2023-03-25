from django import forms
from django.forms import ModelForm

from articleapp.models import Article, ArticleImage

from django.utils.translation import gettext_lazy


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article

        fields = ["title", "place_name", "address", "content"]  # writer는 서버 단에서 작업

        labels = {
            "title": gettext_lazy("Title"),
            "place_name": gettext_lazy("Place Name"),
            "address": gettext_lazy("Address"),
            "content": gettext_lazy("Comment / Memory about this place"),
        }

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title of your article"}),
            "place_name": forms.TextInput(attrs={"placeholder": "Enter the name of your place"}),
            "address": forms.TextInput(attrs={"placeholder": "Enter the address of your place"}),
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

