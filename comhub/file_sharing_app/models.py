from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class File(models.Model):
    title = models.CharField(_("Title for the File"), max_length=50, null=True, blank=True)
    uploader = models.ForeignKey(User, verbose_name=_("uploader"), related_name="uploader", on_delete=models.CASCADE) 
    assigned_to = models.ForeignKey(User, verbose_name=_("assigned_to"), related_name="assigned_to", on_delete=models.CASCADE, null=True, blank=True )
    uploaded_file = models.FileField(_("File"), upload_to='uploads')
    note = models.TextField(_("Note or Reminder"), null=True, blank=True)


    def __str__(self):
        return self.title

    
    