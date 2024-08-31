from django.db import models

from core.apps.companies.entities.company_types import CompanyTypeEntity


class CompanyType(models.Model):
    title = models.CharField(
        verbose_name="Назва компанії",
        max_length=255,
    )

    def to_entity(self) -> CompanyTypeEntity:
        return CompanyTypeEntity(id=self.pk, title=str(self.title))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Тип компанії"
        verbose_name_plural = "Типи компаній"
