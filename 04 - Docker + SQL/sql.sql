from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://user:root@hostname/test_db')