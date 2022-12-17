CREATE TABLE IF NOT EXISTS clients_positions
(
    day date NOT NULL,
    juridical_long integer,
    juridical_short integer,
    physical_long integer,
    physical_short integer,
    contract character(128) COLLATE pg_catalog."default" NOT NULL
)

CREATE TABLE IF NOT EXISTS open_positions
(
    day date NOT NULL,
    juridical_long integer,
    juridical_short integer,
    physical_long integer,
    physical_short integer,
    contract character(128) COLLATE pg_catalog."default" NOT NULL
)
