steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE services (
        id serial PRIMARY KEY,
        barber_id INT REFERENCES accounts (id),
        service_name TEXT NOT NULL,
        price MONEY NOT NULL
    );
        """,
        # "Down" SQL statement
        """
        DROP TABLE profiles;
        """,
    ],
]