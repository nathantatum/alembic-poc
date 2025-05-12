# Alembic POC: Database Migrations and Seeding

## Configuration
### Database Connection
Update the `sqlalchemy.url` in `alembic.ini` with your PostgreSQL connection details:

```
sqlalchemy.url = postgresql://<username>:<password>@<host>:<port>/<database>
```

## Using Alembic
### 1. Initialize Alembic
If Alembic is not already initialized in your project, you can initialize it with:

```
alembic init alembic
```

This creates the `alembic/` directory and the `alembic.ini` configuration file.

### 2. Create a New Migration
To create a new migration script, use the following command:

```
alembic revision --autogenerate -m "Your migration message"
```

The `--autogenerate` flag inspects your SQLAlchemy models and generates a migration script based on detected changes.
The migration script will be created in the `alembic/versions/` directory.

### 3. Apply Migrations
To apply the latest migrations to your database, run:

```
alembic upgrade head
```
* head refers to the latest migration in the migration history.

### 4. Downgrade Migrations
To revert the last migration, run:

```
alembic downgrade -1
```
* You can also specify a specific revision ID to downgrade to:

```
alembic downgrade <revision_id>
```

### 5. View Migration History
To view the migration history, use:

```
alembic history
```

### 6. Check Current Database Version
To check the current version of the database schema, run:

```
alembic current
```

### 7. Manually Edit Migration Scripts
Migration scripts are stored in the `alembic/versions/` directory. You can manually edit these scripts to add custom logic, such as seeding data or performing complex schema changes.

## Seeding Data
After applying migrations, you can seed initial data into the database using the provided scripts.

### Seed Teams and Parks Data
Run the following command to seed data into the teams and parks tables:

```
python db/seed_data.py
```

### Verify Seeded Data
You can verify the data in the database by querying the `mlb.teams` and `mlb.parks` tables:

```
SELECT * FROM mlb.teams;
SELECT * FROM mlb.parks;
```

## Troubleshooting
* **Database Connection Issues**: Ensure the `sqlalchemy.url` in `alembic.ini` is correctly configured with your database credentials.
* **Seeding Errors**: If the seeding script fails, check the error message and ensure the database schema matches the expected structure.
* **Autogenerate Issues**: If `--autogenerate` does not detect changes, ensure your SQLAlchemy models are correctly imported in `alembic/env.py`.

## Additional Resources
* [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)