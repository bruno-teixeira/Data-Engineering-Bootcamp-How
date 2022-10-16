create view vw_first_time as

with first_time as (
	select "date"
		, "rank"
		, artist
		, song
		, row_number() over(partition by artist order by "date") as row_n
	from billboard b 
)
select artist 
	, song 
	, "date"
	, "rank"
from first_time 
where row_n = 1