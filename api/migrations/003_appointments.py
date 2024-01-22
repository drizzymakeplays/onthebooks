steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE appointments (
        id serial PRIMARY KEY,
        client_id INT REFERENCES accounts (id),
        barber_id INT REFERENCES accounts (id),
        appointment_date DATE NOT NULL,
        appointment_time TIME NOT NULL,
        status TEXT NOT NULL DEFAULT 'scheduled' CHECK (
            status IN ('scheduled', 'completed', 'canceled', 'no-show')
        )
    );
        """,
        # "Down" SQL statement
        """
        DROP TABLE appointments;
        """,
    ],
]
