steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE working_hours (
        barber_id INT REFERENCES accounts (id),
        day_of_week TEXT,
        start_time TIME,
        end_time TIME
    );
        """,
        # "Down" SQL statement
        """
        DROP TABLE working_hours;
        """,
    ],
]