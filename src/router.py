from fastapi import APIRouter, FastAPI

from src.group.views import router as group_router
from src.user.views import router as user_router
from src.task.views import router as task_router

router = APIRouter()
router.include_router(group_router)
router.include_router(user_router)
router.include_router(task_router)
