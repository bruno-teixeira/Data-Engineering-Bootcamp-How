drop table if exists artists
;

select distinct artist
into public.artists
FROM PUBLIC.billboard
order by 1
;


