steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE profiles (
        id serial PRIMARY KEY REFERENCES accounts (id),
        display_name TEXT NOT NULL,
        profile_picture TEXT,
        phone_number TEXT,
        shop_address TEXT,
        shop_name TEXT
    );
        """,
        # "Down" SQL statement
        """
        DROP TABLE profiles;
        """,
    ],
]
