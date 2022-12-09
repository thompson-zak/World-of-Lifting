CREATE TABLE powerlifting (
	id bigserial PRIMARY KEY,
	Sex varchar(2) NOT NULL,
	Equipment varchar(20) NOT NULL,
	Age decimal,
	AgeClass varchar(20),
	BodyweightKg decimal,
	WeightClassKg varchar(10),
	Best3SquatKg decimal,
	Best3BenchKg decimal,
	Best3DeadliftKg decimal,
	Place varchar(10) NOT NULL,
	Federation varchar(20) NOT NULL,
	Date date NOT NULL,
	created_date date DEFAULT now() NOT NULL
);