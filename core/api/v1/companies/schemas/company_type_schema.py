from pydantic import BaseModel

from core.apps.companies.entities.company_types import CompanyTypeEntity


class CompanyTypeSchema(BaseModel):
    id: int  # noqa
    title: str

    @staticmethod
    def from_entity(entity: CompanyTypeEntity) -> "CompanyTypeSchema":
        return CompanyTypeSchema(id=entity.id, title=entity.title)


CompanyTypeListSchema = list[CompanyTypeSchema]
