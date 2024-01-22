from models.profiles import ProfileOut
from queries.pool import pool
from typing import List


class ProfileQueries:
    def update_profile(self, profile_info, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    id,
                    profile_info.display_name,
                    profile_info.profile_picture,
                    profile_info.phone_number,
                    profile_info.shop_address,
                    profile_info.shop_name,
                ]
                db.execute(
                    """
                    INSERT INTO profiles(
                        id,
                        display_name,
                        profile_picture,
                        phone_number,
                        shop_address,
                        shop_name
                    )
                    VALUES
                        (%s, %s, %s, %s, %s, %s)
                    RETURNING
                        id,
                        display_name,
                        profile_picture,
                        phone_number,
                        shop_address,
                        shop_name
                    ;
                    """,
                    params,
                )

                record = None
                row = db.fetchone()
                if row is not None:
                    record = {}
                    for i, col in enumerate(db.description):
                        record[col[0]] = row[i]
                return ProfileOut(**record)

    def set_profile_completed(self, id: int, status: bool):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    UPDATE accounts
                    SET profile_completed = %s
                    WHERE id = %s;
                    """,
                    (status, id),
                )

    def update_existing_profile(self, id, profile_info):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    profile_info.display_name,
                    profile_info.profile_picture,
                    profile_info.phone_number,
                    profile_info.shop_address,
                    profile_info.shop_name,
                    id,
                ]
                db.execute(
                    """
                    UPDATE profiles
                    SET
                        display_name = %s,
                        profile_picture = %s,
                        phone_number = %s,
                        shop_address = %s,
                        shop_name = %s
                    WHERE id = %s;
                    """,
                    params,
                )
                if db.rowcount > 0:
                    return True
                else:
                    return None

    def list_profiles(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, display_name, profile_picture, phone_number, shop_address, shop_name
                    FROM profiles;
                    """
                )
                profiles = db.fetchall()

        return [
            ProfileOut(
                id=record[0],
                display_name=record[1],
                profile_picture=record[2],
                phone_number=record[3],
                shop_address=record[4],
                shop_name=record[5],
            )
            for record in profiles
        ]

    def get_profile(self, display_name: str):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, display_name, profile_picture, phone_number, shop_address, shop_name
                    FROM profiles
                    WHERE display_name = %s;
                    """,
                    (display_name,),
                )
                profile = db.fetchone()

        if profile:
            return ProfileOut(
                id=profile[0],
                display_name=profile[1],
                profile_picture=profile[2],
                phone_number=profile[3],
                shop_address=profile[4],
                shop_name=profile[5],
            )
        else:
            return None

    def get_my_profile(self, profile_id: int):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, display_name, profile_picture, phone_number, shop_address, shop_name
                    FROM profiles
                    WHERE id = %s;
                    """,
                    (profile_id,),
                )
                profile = db.fetchone()

        if profile:
            return ProfileOut(
                id=profile[0],
                display_name=profile[1],
                profile_picture=profile[2],
                phone_number=profile[3],
                shop_address=profile[4],
                shop_name=profile[5],
            )
        else:
            return None
