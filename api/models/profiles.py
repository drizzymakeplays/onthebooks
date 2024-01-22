from pydantic import BaseModel


class ProfileIn(BaseModel):
    display_name: str
    profile_picture: str
    phone_number: str
    shop_address: str
    shop_name: str


class ProfileOut(BaseModel):
    id: int
    profile_picture: str
    display_name: str
    phone_number: str
    shop_address: str
    shop_name: str


class UpdateProfileResponse(BaseModel):
    success: bool
    message: str