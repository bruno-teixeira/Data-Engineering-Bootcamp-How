drop table if exists songs
;

select distinct artist, song
into public.songs
FROM PUBLIC.billboard
order by 1, 2