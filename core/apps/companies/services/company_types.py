from abc import ABC, abstractmethod
from typing import Iterable
from core.apps.companies.entities.company_types import CompanyTypeEntity
from core.apps.companies.models.company_types import CompanyType as CompanyTypeModel


class BaseCompanyTypeService(ABC):
    @abstractmethod
    def get_list_company_types(self) -> Iterable[CompanyTypeEntity]:
        ...


class ORMCompanyTypeService(BaseCompanyTypeService):
    def get_list_company_types(self) -> Iterable[CompanyTypeEntity]:
        qs = CompanyTypeModel.objects.filter()
        return [company_type.to_entity() for company_type in qs]
