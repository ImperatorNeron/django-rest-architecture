from django.http import HttpRequest
from ninja import Router, Query

from core.api.pagination import PaginationOut, PaginationIn
from core.api.schemas import ListPaginatedResponse, ApiResponse
from core.api.v1.companies.schemas.company_type_schema import CompanyTypeSchema

from core.apps.companies.services.company_types import (
    BaseCompanyTypeService,
    ORMCompanyTypeService,
)

router = Router(tags=["Companies"])


@router.get("/types", response=ApiResponse[ListPaginatedResponse[CompanyTypeSchema]])
def get_company_type_list_handler(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
) -> ApiResponse[ListPaginatedResponse[CompanyTypeSchema]]:
    service: BaseCompanyTypeService = ORMCompanyTypeService()
    types_list = service.get_list_company_types(pagination_in)
    items = [CompanyTypeSchema.from_entity(obj) for obj in types_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=service.get_company_types_count(),
    )
    return ApiResponse(
        data=ListPaginatedResponse(
            items=items,
            pagination=pagination_out,
        )
    )
