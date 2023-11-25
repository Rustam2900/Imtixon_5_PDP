from aiogram import Router
from .start import router as start_router
from .orders import router as orders_router

router = Router()

router.include_router(start_router)
router.include_router(orders_router)
