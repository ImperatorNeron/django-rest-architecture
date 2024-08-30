from ninja import Router
from .companies.handlers import router as companies_router

router = Router()

router.add_router("/companies", companies_router)