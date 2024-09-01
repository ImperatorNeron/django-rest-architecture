import pytest
from tests.factories.company_type import CompanyTypeModelFactory

from core.api.pagination import PaginationIn
from core.apps.companies.services.company_types import BaseCompanyTypeService


@pytest.mark.django_db
def test_get_company_types_count_zero(company_type_service: BaseCompanyTypeService):
    """Test company types zero with no types in database."""
    company_type_count = company_type_service.get_company_types_count()
    assert company_type_count == 0, f"{company_type_count=}"


@pytest.mark.django_db
def test_get_company_types_count_exists(company_type_service: BaseCompanyTypeService):
    """Test company types count exists with types in database."""
    expected_count = 5
    CompanyTypeModelFactory.create_batch(size=expected_count)
    company_type_count = company_type_service.get_company_types_count()
    assert company_type_count == expected_count, f"{company_type_count=}"


@pytest.mark.django_db
def test_get_company_types_all(company_type_service: BaseCompanyTypeService):
    """Test company types count exists with types in database."""
    count = 5
    company_types = CompanyTypeModelFactory.create_batch(size=count)
    company_types_titles = {company_type.title for company_type in company_types}

    fetched_company_types = company_type_service.get_list_company_types(PaginationIn())
    fetched_titles = {company_type.title for company_type in fetched_company_types}

    assert len(fetched_titles) == count, f'{fetched_titles=}'
    assert company_types_titles == fetched_titles, f'{company_types_titles=}'
