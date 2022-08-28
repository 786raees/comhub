from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.fields import StatusField
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """
    Default custom user model for comhub.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    address = TextField(_("Address"), blank=True)
    phone_number = PhoneNumberField(_("User's Phone Number"), blank=True)
    user_type_choices = Choices('Admin','Suplier','Customer',)
    user_type = StatusField(choices_name='user_type_choices')
    customer_of = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
