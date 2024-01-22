from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from models.accounts import (
    AccountToken,
    AccountIn,
    AccountForm,
    DuplicateAccountError,
)
from psycopg.errors import UniqueViolation
from authenticator import authenticator
from pydantic import BaseModel
from queries.accounts import AccountQueries


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.get("/api/accounts/")
async def get_account():
    pass


@router.post(
    "/api/accounts/register/", response_model=AccountToken | HttpError
)
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    repo: AccountQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = repo.create(info, hashed_password=hashed_password)
        print(account)

    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    except UniqueViolation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists.",
        )

    form = AccountForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


@router.put("/api/accounts/update/")
async def update_account():
    pass


@router.delete("/api/accounts/delete/")
async def delete_account():
    pass
