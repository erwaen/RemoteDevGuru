import fastapi


from src.api.routes.authentication import router as auth_router
from src.api.routes.chat import router as chat_router
from src.api.routes.history import router as history_router
from src.api.routes.support import router as support_router

router = fastapi.APIRouter()

router.include_router(router=auth_router)
router.include_router(router=chat_router)
router.include_router(router=history_router)
router.include_router(router=support_router)
