from models.profiles import ProfileOut
from queries.pool import pool


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

                # Check if the update was successful (you can add error handling as needed)
                if db.rowcount > 0:
                    return True
                else:
                    return None
