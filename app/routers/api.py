from fastapi import APIRouter

from app.routers import blacklist as blacklistRouter, number as numberRouter

router = APIRouter()

router.include_router(blacklistRouter.router)
router.include_router(numberRouter.router)
