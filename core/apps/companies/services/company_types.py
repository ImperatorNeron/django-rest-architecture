from abc import ABC, abstractmethod
from typing import Iterable

from core.api.pagination import PaginationIn
from core.apps.companies.entities.company_types import CompanyTypeEntity
from core.apps.companies.models.company_types import CompanyType as CompanyTypeModel


class BaseCompanyTypeService(ABC):
    @abstractmethod
    def get_list_company_types(self, pagination: PaginationIn) -> Iterable[CompanyTypeEntity]:
        ...

    @abstractmethod
    def get_company_types_count(self) -> int:
        ...


class ORMCompanyTypeService(BaseCompanyTypeService):
    def get_list_company_types(
        self, pagination: PaginationIn
    ) -> Iterable[CompanyTypeEntity]:
        qs = CompanyTypeModel.objects.filter()[
            pagination.offset: pagination.offset + pagination.limit
        ]
        return [company_type.to_entity() for company_type in qs]

    def get_company_types_count(self) -> int:
        return CompanyTypeModel.objects.filter().count()
