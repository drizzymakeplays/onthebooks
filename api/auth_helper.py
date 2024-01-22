from typing import Optional
from fastapi import HTTPException, status, Depends
from authenticator import authenticator

def get_current_user_data(
    account_data: Optional[dict] = Depends(authenticator.try_get_current_account_data),
):
    if account_data:
        return {
            **account_data,
            "profile_completed": account_data.get("profile_completed", False),
        }
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
