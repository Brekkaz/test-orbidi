create table if not exists category_location (
    id UUID not null default (uuid_generate_v4()),
    category_id UUID not null,
    location_id UUID not null,
    reviewed timestamptz not null default now(),
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    deleted_at timestamptz,
    primary key (id),
    foreign key (category_id) REFERENCES category(id),
    foreign key (location_id) REFERENCES location(id)
);