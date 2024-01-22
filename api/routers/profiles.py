from fastapi import (
    Depends,
    HTTPException,
    status,
    APIRouter,
)
from models.profiles import (
    ProfileIn,
    ProfileOut,
    UpdateProfileResponse,
)

from auth_helper import get_current_user_data
from pydantic import BaseModel
from queries.profiles import ProfileQueries
from typing import List, Union


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.get("/api/profiles/", response_model=List[ProfileOut] | HttpError)
async def list_profiles(
    repo: ProfileQueries = Depends(),
):
    profiles = repo.list_profiles()

    if not profiles:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No profiles found",
        )

    return profiles


@router.get(
    "/api/profiles/{profile_id}/", response_model=ProfileOut | HttpError
)
async def get_profile(
    profile_id: int,
    repo: ProfileQueries = Depends(),
):
    profile = repo.get_profile(profile_id)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile does not exist",
        )

    return profile


@router.get("/api/profiles/my-profile/", response_model=ProfileOut | HttpError)
async def get_my_profile(
    current_user_data: dict = Depends(get_current_user_data),
    repo: ProfileQueries = Depends(),
):
    profile_id = current_user_data.get("id")

    if not profile_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    profile = repo.get_my_profile(profile_id)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile does not exist",
        )

    return profile


@router.post(
    "/api/profiles/complete-profile", response_model=ProfileOut | HttpError
)
async def complete_profile(
    profile_info: ProfileIn,
    current_user: dict = Depends(get_current_user_data),
    repo: ProfileQueries = Depends(),
):
    user_id = current_user.get("id")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    profile_completed = current_user.get("profile_completed", False)

    if profile_completed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile is already completed",
        )

    updated_profile = repo.update_profile(profile_info, user_id)
    repo.set_profile_completed(user_id, True)
    return updated_profile


@router.put(
    "/api/profiles/update-profile/",
    response_model=UpdateProfileResponse | HttpError,
)
async def update_profile(
    profile_info: ProfileIn,
    current_user: dict = Depends(get_current_user_data),
    repo: ProfileQueries = Depends(),
):
    user_id = current_user.get("id")
    print("user id:", user_id)
    print("profile info:", profile_info)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    updated = repo.update_existing_profile(user_id, profile_info)

    print("updated Profile:", updated)

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )
    elif updated:
        return UpdateProfileResponse(
            success=True, message="Profile updated successfully"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update profile",
        )
