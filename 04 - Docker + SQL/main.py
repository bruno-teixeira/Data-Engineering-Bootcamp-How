from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql+psycopg2://root:root@localhost/test_db')

#Processo executando select

sql = '''
select * from vw_first_time;
'''

df = pd.read_sql_query(sql, engine)

df.head()

#Processo executando script de drop, create e insert

sql_create_tb_artists = '''
drop table if exists artists
;

select distinct artist
into public.artists
FROM PUBLIC.billboard
order by 1
;
'''

engine.execute(sql_create_tb_artists)

sql_tb_artists_select = '''
select * from artists;
'''

pd.read_sql_query(sql, engine).head()
