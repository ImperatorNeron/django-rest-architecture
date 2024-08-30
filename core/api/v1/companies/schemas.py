from typing import List

from pydantic import BaseModel


class CompanyTypeSchema(BaseModel):
    id: int
    title: str


class CompanyTypeListSchema(BaseModel):
    company_types: List[CompanyTypeSchema]
