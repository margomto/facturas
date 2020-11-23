from django import forms
from crispy_forms.layout import Layout
from django.forms import Form, CharField
from crispy_forms.helper import FormHelper

from django_crispy_bulma.layout import IconField

class SignUpForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            IconField("username", icon_prepend="user"),
        )

    username = CharField(
        label="Username",
        required=True,
    )