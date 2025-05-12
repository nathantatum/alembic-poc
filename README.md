# alembic_poc

This project demonstrates the use of Alembic for managing database schema migrations and seeding initial data for a single-database configuration. It includes a PostgreSQL database setup with tables for `teams` and `parks`, along with scripts to seed initial data into these tables.

## Project Structure

```
alembic_poc/
├── alembic.ini # Alembic configuration file
├── db/
│ ├── data/
│ │ ├── seed_data.py # Script to seed all initial data
│ │ ├── teams.py # Script to seed data into the 'teams' table
│ │ ├── parks.py # Script to seed data into the 'parks' table
│ ├── models/
│ │ ├── teams.py # SQLAlchemy model for the 'teams' table
│ │ ├── parks.py # SQLAlchemy model for the 'parks' table
│ ├── versions/ # Directory for migration scripts
│ ├── base.py # Base SQLAlchemy model
│ ├── env.py # Alembic environment configuration

```

## Features

1. **Database Schema Management**:
   - Uses Alembic to manage schema migrations.
   - Migration scripts are stored in the `alembic/versions/` directory.

2. **Seeding Initial Data**:
   - Includes scripts to seed initial data into the `teams` and `parks` tables.
   - Data is inserted or updated using PostgreSQL's `INSERT ... ON CONFLICT` syntax.  Note: `MERGE` is supported in Postgres v.15 but not in Aurora which substantiates this design decision.

3. **PostgreSQL Configuration**:
   - The project is configured to use a PostgreSQL database.
   - Connection details are specified in the `alembic.ini` file.

## Prerequisites

- Python 3.9 or higher
- PostgreSQL database
- Install dependencies:
  ```bash
  pip install -r requirements.txt