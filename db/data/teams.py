from sqlalchemy import text

def seed_teams(session):
    data = [
        {"id": 1, "name": "New York Yankees", "abbreviation": "NYY", "city": "New York", "state": "NY", "founded_date": "1901-01-01"},
        {"id": 2, "name": "Los Angeles Dodgers", "abbreviation": "LAD", "city": "Los Angeles", "state": "CA", "founded_date": "1883-01-01"},
        {"id": 3, "name": "Chicago Cubs", "abbreviation": "CHC", "city": "Chicago", "state": "IL", "founded_date": "1876-01-01"},
    ]

    try:
        for data in data:
            session.execute(
                text("""
                    INSERT INTO mlb.teams (id, name, abbreviation, city, state, founded_date)
                    VALUES (:id, :name, :abbreviation, :city, :state, :founded_date)
                    ON CONFLICT (id) DO UPDATE
                    SET name = EXCLUDED.name,
                        abbreviation = EXCLUDED.abbreviation,
                        city = EXCLUDED.city,
                        state = EXCLUDED.state,
                        founded_date = EXCLUDED.founded_date
                """),
                data
            )
        session.commit()
    
    except Exception as e:
        session.rollback()
        print(f"Error during upsert: {e}")