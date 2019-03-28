from django.db import models


class Chore(models.Model):
    choreName = models.CharField(max_length=50)
    choreComplete = models.BooleanField()
    person = models.ManyToManyField("Person")

    class Meta:
        verbose_name = _("Chore")
        verbose_name_plural = _("Chores")

    def __str__(self):
        return self.choreName

    def get_absolute_url(self):
        return reverse("Chore_detail", kwargs={"pk": self.pk})


class Person(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})
