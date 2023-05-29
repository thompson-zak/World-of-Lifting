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

CREATE TABLE running (
	id bigserial PRIMARY KEY,
	Sex varchar(2) NOT NULL,
	Age decimal NOT NULL,
	Event varchar(20) NOT NULL,
	FinishTime integer NOT NULL,
	DataSource varchar(20) NOT NULL,
	SourceId integer NOT NULL
);