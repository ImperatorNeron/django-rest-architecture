from django.http import HttpRequest
from ninja import Router

from core.api.v1.companies.schemas import CompanyTypeListSchema

router = Router(tags=["Companies"])


@router.get("/types", response=CompanyTypeListSchema)
def get_product_list_handler(request: HttpRequest) -> CompanyTypeListSchema:
    return []
