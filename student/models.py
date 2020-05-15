from django.db import models

# Create your models here.
class student(models.Model):

    name = models.models.CharField(_("name"), max_length=50)
    

    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)