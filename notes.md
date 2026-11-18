Connection: Establishes communication between your Python program and PostgreSQL.



Cursor: Allows your Python program to send SQL commands to PostgreSQL and retrieve results.

Why do this instead of joining strings manually? Because parameterized queries help protect our database against SQL injection and handle values safely.