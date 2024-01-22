from models.accounts import AccountOutWithHashedPassword
from queries.pool import pool


class AccountQueries:
    def get(self, username: str) -> AccountOutWithHashedPassword:
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT *
                    FROM accounts
                    WHERE username = %s;
                    """,
                    (username,),
                )
                try:
                    record = None
                    row = db.fetchone()
                    if row is not None:
                        record = {}
                        for i, col in enumerate(db.description):
                            record[col[0]] = row[i]
                    return AccountOutWithHashedPassword(**record)
                except Exception:
                    return {"message": "Account not found"}
    def create(self, data, hashed_password) -> AccountOutWithHashedPassword:
        with pool.connection() as conn:
            with conn.cursor() as db:

                params = [
                    data.first_name,
                    data.last_name,
                    data.username,
                    data.birthday,
                    data.email,
                    data.role,
                    hashed_password,
                ]
                db.execute(
                    """
                    INSERT INTO accounts(
                        first_name,
                        last_name,
                        username,
                        birthday,
                        email,
                        role,
                        hashed_password
                    )
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING
                        id,
                        first_name,
                        last_name,
                        username,
                        birthday,
                        email,
                        role,
                        hashed_password
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
                    print(record)
                return AccountOutWithHashedPassword(**record)

