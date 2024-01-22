steps = [
    [
        # "Up" SQL statement
        """
        ALTER TABLE accounts
        ADD COLUMN profile_completed BOOLEAN DEFAULT FALSE;
        """,
        # "Down" SQL statement
        """
        ALTER TABLE accounts
        DROP COLUMN profile_completed;
        """,
    ],
]