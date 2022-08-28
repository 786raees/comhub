import uuid
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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