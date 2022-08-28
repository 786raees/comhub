from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from comhub.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {"fields": ("username", 'password1', 'password2')}),
        (_("Personal info"), {"fields": ("name", "email",
                                         "address",
                                         "phone_number",
                                         "customer_of",
                                         "user_type")}),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email",
                                         "address",
                                         "phone_number",
                                         "customer_of",
                                         "user_type")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
    def get_list_filter(self, request):
        new_filter = super().get_list_filter(request) + ('user_type',)
        return new_filter
