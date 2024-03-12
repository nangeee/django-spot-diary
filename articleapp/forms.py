from django import forms
from django.forms import ModelForm

from articleapp.models import Article

from django.utils.translation import gettext_lazy


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article

        fields = ["title", "project", "image", "content"]  # writer, place는 서버 단에서 작업

        labels = {
            "title": gettext_lazy("Title"),
            "project": gettext_lazy("Project"),
            "image": gettext_lazy("Image"),
            "content": gettext_lazy("Content"),
        }

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title of your article"}),
            "content": forms.Textarea(attrs={"placeholder": "Write something"})
        }

        error_messages = {
            "title": {
                "max_length": gettext_lazy("제목은 20자 이내로 입력해주세요.")
            }
        }


# class ArticleImageForm(ModelForm):
#     class Meta:
#         model = ArticleImage
#
#         fields = ["image", ]  # post(article)는 서버 단에서 작업
#
#         labels = {
#             "image": gettext_lazy("Image")
#         }

