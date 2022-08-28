import uuid
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from file_sharing_app.models import File

User = get_user_model()

class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = str(uuid.uuid1()).split("-")[-1]
        self.fields['password1'].widget.attrs.update({'value':password})
        self.fields['password2'].widget.attrs.update({'value':password})

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('title','uploaded_file','note',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['note'].widget.attrs.update({'rows':3})
