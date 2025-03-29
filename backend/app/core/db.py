from sqlmodel import create_engine

engine = create_engine("postgresql+psycopg2://admin:admin@localhost/budget_db")