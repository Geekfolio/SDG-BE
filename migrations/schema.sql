-- Enum Tables, to be converted to proper enums when migrating to pg or mysql
CREATE TABLE  IF NOT EXISTS enum_department(
  department TEXT PRIMARY KEY
);

INSERT INTO enum_department (department) VALUES ('AIML');
INSERT INTO enum_department (department) VALUES ('ECE');
INSERT INTO enum_department (department) VALUES ('EEE');
INSERT INTO enum_department (department) VALUES ('CSE');
INSERT INTO enum_department (department) VALUES ('IT');
INSERT INTO enum_department (department) VALUES ('CYBER');
INSERT INTO enum_department (department) VALUES ('MECH');
INSERT INTO enum_department (department) VALUES ('MCT');
INSERT INTO enum_department (department) VALUES ('AIDS');
INSERT INTO enum_department (department) VALUES ('BIO');
INSERT INTO enum_department (department) VALUES ('CSBS');
INSERT INTO enum_department (department) VALUES ('CIVIL');

-- ...more to add

CREATE TABLE IF NOT EXISTS enum_years(
  year INTEGER PRIMARY KEY
);

INSERT INTO enum_years (year) VALUES (1);
INSERT INTO enum_years (year) VALUES (2);
INSERT INTO enum_years (year) VALUES (3);
INSERT INTO enum_years (year) VALUES (4);

CREATE TABLE IF NOT EXISTS enum_event_type(
  type VARCHAR(30) PRIMARY KEY
);

INSERT INTO enum_event_type (type) VALUES('Hackathon');
INSERT INTO enum_event_type (type) VALUES('Coding Challenge');
INSERT INTO enum_event_type (type) VALUES('Workshop');

-- User schema 

CREATE TABLE IF NOT EXISTS users (
  email TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  authority INTEGER NOT NULL CHECK(authority IN (1,2,3,4)),
  department TEXT, -- would be null for ADMINISTRATOR
  reg TEXT, -- would be present only for STUDENT
  batch TEXT -- would be present only for BATCH
  -- fuck i know this is not scalable, but would scale for this 2 day hack
);

INSERT INTO users (email, name, authority, department, reg, batch) VALUES ("ajayb.ece2023@citchennai.net", "Ajay Balaji Prasad", 4, 'ECE', '213223106001', '2023');
INSERT INTO users (email, name, authority, department, reg, batch) VALUES ("lovelindhonijb.aiml2023@citchennai.net", "Lovelin Dhoni JB", 4, 'AIML', '23AM065', '2023');

CREATE TABLE IF NOT EXISTS permissions(
  permission TEXT PRIMARY KEY,
  needed_authority INTEGER CHECK(needed_authority IN (1,2,3,4))
);

-- Events Schema 
CREATE TABLE events(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT,
  description TEXT,
  event_type VARCHAR,
  team_size INTEGER,
  start DATETIME,
  end DATETIME,
  participants INTEGER DEFAULT 0,
  status TEXT,
  authority INTEGER CHECK(authority IN (1,2,3,4)),
  FOREIGN KEY(event_type) REFERENCES enum_event_type(type),
  FOREIGN KEY(email) REFERENCES users(email)
);

CREATE TABLE event_departments(
  event_id INTEGER,
  department TEXT,
  FOREIGN KEY(event_id) REFERENCES events(id),
  FOREIGN KEY(department) REFERENCES enum_department(department)
);

CREATE TABLE event_years(
  event_id INTEGER,
  year INTEGER,
  FOREIGN KEY(event_id) REFERENCES events(id),
  FOREIGN KEY(year) REFERENCES enum_year(year)
);
