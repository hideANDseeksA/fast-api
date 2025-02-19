from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={
        "database": "postgres",     # Ensure this is correct
        "user": "postgres.womlhdbniiweqaeevwll",         # PostgreSQL username
        "password": "kf5ISjFnV5sad3yI", # PostgreSQL password
        "host": "aws-0-ap-southeast-1.pooler.supabase.com",            # Ensure this is correct
        "port": 6543,                   # PostgreSQL default port
    }
)
