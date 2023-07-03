from django.db import models


class ZodiacBase(models.Model):

    first_date = models.DateField()
    last_date = models.DateField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Zodiacs(models.Model):
    class Status(models.IntegerChoices):
        ARCHIVED = 0
        AVAILABLE = 1

    name = models.CharField(max_length=100)
    zodiac_name = models.ForeignKey(
        ZodiacBase,
        on_delete=models.PROTECT,
        related_name="zodiacs",
    )
    date_bth = models.DateField()
    status = models.IntegerField(
        choices=Status.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Zodiac <{self.pk}, {self.name!r}>"
