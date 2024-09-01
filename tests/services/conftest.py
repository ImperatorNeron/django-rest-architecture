import pytest

from core.apps.companies.services.company_types import (
    BaseCompanyTypeService,
    ORMCompanyTypeService,
)


@pytest.fixture
def company_type_service() -> BaseCompanyTypeService:
    return ORMCompanyTypeService()
