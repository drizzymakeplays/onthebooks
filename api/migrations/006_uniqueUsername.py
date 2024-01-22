steps = [
    [
        # "Up" SQL statement
        """
        ALTER TABLE accounts
        ADD CONSTRAINT unique_username UNIQUE (username);
        """,
        # "Down" SQL statement
        """
        ALTER TABLE accounts
        DROP CONSTRAINT unique_username;
        """,
    ],
]