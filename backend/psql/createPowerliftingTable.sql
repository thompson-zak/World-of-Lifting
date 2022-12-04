CREATE TABLE powerlifting (
	id bigserial PRIMARY KEY,
	sex varchar(2) NOT NULL,
	equipment varchar(20) NOT NULL,
	age decimal,
	age_class varchar(20),
	best_squat_kg integer,
	best_bench_kg integer,
	best_deadlift_kg integer,
	place varchar(10) NOT NULL,
	federation varchar(20) NOT NULL,
	meet_date date NOT NULL
);