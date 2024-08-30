from django.db import models


class CompanyType(models.Model):
    title = models.CharField(
        verbose_name="Назва компанії",
        max_length=255,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Тип компанії"
        verbose_name_plural = "Типи компаній"
