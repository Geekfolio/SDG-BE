-- convert this to an enum when migrating to postgres or mysql
CREATE TABLE  IF NOT EXISTS enum_department(
  department TEXT PRIMARY KEY
);

INSERT INTO enum_department (department) VALUES ('CSE-AIML');
INSERT INTO enum_department (department) VALUES ('ECE');
INSERT INTO enum_department (department) VALUES ('EEE');
INSERT INTO enum_department (department) VALUES ('CSE');
INSERT INTO enum_department (department) VALUES ('CSE-CS');
INSERT INTO enum_department (department) VALUES ('IT');
-- ...more to add

CREATE TABLE IF NOT EXISTS roles(
  -- convert this to an enum when migrating to postgres or mysql
  role TEXT PRIMARY KEY CHECK(role IN ('ADMINISTRATOR', 'COORDINATOR', 'FACULTY', 'STUDENT')),
  authority INTEGER NOT NULL CHECK(authority IN (1,2,3,4))
);

INSERT INTO roles (role, authority) VALUES ('ADMINISTRATOR', 4);
INSERT INTO roles (role, authority) VALUES ('COORDINATOR', 3);
INSERT INTO roles (role, authority) VALUES ('FACULTY', 2);
INSERT INTO roles (role, authority) VALUES ('STUDENT', 1);

CREATE TABLE IF NOT EXISTS users (
  email TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  role TEXT NOT NULL,
  department TEXT, -- would be null for ADMINISTRATOR
  reg TEXT, -- would be present only for STUDENT
  batch TEXT, -- would be present only for BATCH
  -- fuck i know this is not scalable, but would scale for this 2 day hack
  FOREIGN KEY(role) REFERENCES roles(role)
);

CREATE TABLE IF NOT EXISTS permissions(
  permission TEXT PRIMARY KEY,
  needed_authority INTEGER,
  FOREIGN KEY(needed_authority) REFERENCES roles(authority)
);
