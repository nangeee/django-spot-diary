from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import password_validators_help_texts
from django.utils.functional import lazy
from django.utils.html import format_html_join, format_html


def _password_validators_help_text_html(password_validators=None):
    """
    Return an HTML string with all help texts of all configured validators
    in an <ul>.
    """
    help_texts = password_validators_help_texts(password_validators)
    help_items = format_html_join(
        "", "+ {}<br>", ((help_text,) for help_text in help_texts)
    )
    return format_html("{}", help_items) if help_items else ""


password_validators_help_text_html = lazy(_password_validators_help_text_html, str)


class UserCreationForm2(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].help_text = password_validators_help_text_html()


class AccountUpdateForm(UserCreationForm2):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = True  # ID 변경 불가능하도록 disabled 시켜줌
        self.fields["username"].help_text = None




