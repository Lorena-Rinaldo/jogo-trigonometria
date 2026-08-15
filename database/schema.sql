create table if not exists players (
  id uuid unique not null default gen_random_uuid(),
  normalized_name text primary key,
  name text not null,
  character_id integer not null,
  created_at timestamp with time zone default now(),
  updated_at timestamp with time zone default now()
);

alter table players add column if not exists id uuid default gen_random_uuid();
update players set id = gen_random_uuid() where id is null;
alter table players alter column id set not null;
create unique index if not exists players_id_unique on players(id);

create table if not exists player_progress (
  normalized_name text primary key references players(normalized_name) on delete cascade,
  current_stage integer not null default 1,
  score integer not null default 0,
  wrong_answers integer not null default 0,
  answered_questions jsonb not null default '[]'::jsonb,
  completed_stages jsonb not null default '[]'::jsonb,
  unlocked_codes jsonb not null default '[]'::jsonb,
  hints_used jsonb not null default '{}'::jsonb,
  awaiting_final_code boolean not null default false,
  final_code_validated boolean not null default false,
  completed boolean not null default false,
  game_over boolean not null default false,
  updated_at timestamp with time zone default now()
);
