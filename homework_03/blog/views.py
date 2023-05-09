from fastapi import APIRouter

router = APIRouter(
    tags=["Ping"],
)


@router.get(
    "/",
    status_code=200
)
def get_pings(
):
    return {
        "message": "pong"
    }