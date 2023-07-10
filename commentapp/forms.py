from django.forms import ModelForm

from commentapp.models import Comment

"""
메타 데이터는 다른 데이터에 대한 정보를 제공하는 특정 데이터 집합을 나타냅니다. 
Django에서는 Django 모델을 사용하여 데이터베이스의 테이블과 해당 필드를 설계합니다. 
모델 자체에 대한 데이터를 추가해야하는 경우 Meta 클래스를 사용.
Meta클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용 가능. 
Django 모델에Meta클래스를 추가하는 것은 전적으로 선택 사항임.

https://www.delftstack.com/ko/howto/django/class-meta-in-django/
"""


class CommentCreationForm(ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]  # article, writer는 서버 단에서 작업
