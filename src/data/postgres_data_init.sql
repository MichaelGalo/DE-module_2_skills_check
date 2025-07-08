-- Step 1: Create Teams table
CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(100) NOT NULL,
    coach_name VARCHAR(100),
    captain_id INT,
    founded_year INT,
    conference VARCHAR(20) CHECK (conference IN ('Eastern', 'Western'))
);

-- Step 2: Create Players table
CREATE TABLE players (
player_id SERIAL PRIMARY KEY,
team_id INT NOT NULL,
player_name VARCHAR(100) NOT NULL,
position VARCHAR(20) NOT NULL,
skill_level INT CHECK (skill_level BETWEEN 1 AND 10),
jersey_number INT CHECK (jersey_number BETWEEN 1 AND 99),
is_captain BOOLEAN DEFAULT FALSE,
FOREIGN KEY (team_id) REFERENCES teams(team_id),
UNIQUE(team_id, jersey_number)
);

-- Step 3: Add captain constraint
ALTER TABLE teams
ADD CONSTRAINT fk_team_captain
FOREIGN KEY (captain_id) REFERENCES players(player_id);

-- Step 4: Create Games table
CREATE TABLE games (
game_id SERIAL PRIMARY KEY,
host_team_id INT NOT NULL,
guest_team_id INT NOT NULL,
game_date DATE NOT NULL,
host_score INT DEFAULT 0,
guest_score INT DEFAULT 0,
FOREIGN KEY (host_team_id) REFERENCES teams(team_id),
FOREIGN KEY (guest_team_id) REFERENCES teams(team_id),
CHECK (host_team_id != guest_team_id)
);

INSERT INTO teams (team_name, city, coach_name, founded_year, conference) VALUES
('Toronto Maple Leafs', 'Toronto', 'Sheldon Keefe', 1917, 'Eastern'),
('Edmonton Oilers', 'Edmonton', 'Jay Woodcroft', 1972, 'Western');

INSERT INTO players (team_id, player_name, position, skill_level, jersey_number, is_captain) VALUES
(1, 'Auston Matthews', 'Center', 10, 34, FALSE),
(1, 'John Tavares', 'Center', 9, 91, TRUE),
(2, 'Connor McDavid', 'Center', 10, 97, TRUE);

-- Update team captains
UPDATE teams SET captain_id = 2 WHERE team_id = 1;
UPDATE teams SET captain_id = 3 WHERE team_id = 2;

SELECT t.team_name, p.player_name as captain
FROM teams t
JOIN players p ON t.captain_id = p.player_id;
