drop table if exists public.billboard;

create table public.billboard (
	"date" date null,
	"rank" int4 null,
	"song" varchar(500) null,
	"artist" varchar(500) null,
	"last-week" int4 null,
	"peak-rank" int4 null,
	"weeks-on-board" int4 null
); 
