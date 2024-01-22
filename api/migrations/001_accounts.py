steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE accounts (
        id serial PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        username TEXT NOT NULL,
        birthday TEXT NOT NULL,
        email TEXT NOT NULL,
        hashed_password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'client' CHECK (
            role IN ('barber', 'client')
        )
    );
        """,
        # "Down" SQL statement
        """
        DROP TABLE accounts;
        """,
    ],
]
