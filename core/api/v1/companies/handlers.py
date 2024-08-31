from django.http import HttpRequest
from ninja import Router

from core.api.v1.companies.schemas.company_type_schema import (
    CompanyTypeListSchema,
    CompanyTypeSchema,
)
from core.apps.companies.services.company_types import (
    BaseCompanyTypeService,
    ORMCompanyTypeService,
)

router = Router(tags=["Companies"])


@router.get("/types", response=CompanyTypeListSchema)
def get_company_type_list_handler(request: HttpRequest) -> CompanyTypeListSchema:
    service: BaseCompanyTypeService = ORMCompanyTypeService()
    company_types_list = service.get_list_company_types()
    return [CompanyTypeSchema.from_entity(obj) for obj in company_types_list]
