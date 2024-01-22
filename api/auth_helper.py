from typing import Optional
from fastapi import HTTPException, status, Depends
from authenticator import authenticator


def get_current_user_data(
    account_data: Optional[dict] = Depends(
        authenticator.try_get_current_account_data
    ),
):
    if account_data:
        user_id = account_data.get("id")
        profile_id = account_data.get("profile_id")
        return {
            **account_data,
            "profile_completed": account_data.get("profile_completed", False),
            "user_id": user_id,
            "profile_id": profile_id,
        }
    print("account data:", account_data)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated"
    )
