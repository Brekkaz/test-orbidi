create table if not exists location (
    id UUID not null default (uuid_generate_v4()),
    name varchar(50) UNIQUE not null,
    latitude float not null,
    longitude float not null,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    deleted_at timestamptz,
    primary key (id)
);