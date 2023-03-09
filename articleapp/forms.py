from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article

        fields = ["title", "place_name", "address", "content"]  # writer는 서버 단에서 작업업