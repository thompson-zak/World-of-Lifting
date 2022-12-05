CREATE TABLE powerlifting (
	id bigserial PRIMARY KEY,
	sex varchar(2) NOT NULL,
	equipment varchar(20) NOT NULL,
	age decimal,
	age_class varchar(20),
	best_squat_kg decimal,
	best_bench_kg decimal,
	best_deadlift_kg decimal,
	place varchar(10) NOT NULL,
	federation varchar(20) NOT NULL,
	meet_date date NOT NULL,
	created_date date DEFAULT now() NOT NULL
);