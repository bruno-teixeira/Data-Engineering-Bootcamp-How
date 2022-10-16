create view vw_first_time_top_rank as

with first_rank as (
	select "date"
		, "rank"
		, artist
		, song
		, row_number() over(partition by artist order by "date") as row_n
	from billboard b 
	where "rank" = 1
)
select artist 
	, song 
	, "date"
	, "rank"
from first_rank 
where row_n = 1