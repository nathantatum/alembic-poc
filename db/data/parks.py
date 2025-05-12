from sqlalchemy import text

def seed_parks(session):
    data = [
        {"id": 1, "name": "Yankee Stadium", "team_id": 1, "city": "New York", "state": "NY", "capacity": 46537, "opened_date": "2009-01-01"},
        {"id": 2, "name": "Dodger Stadium", "team_id": 2, "city": "Los Angeles", "state": "CA", "capacity": 56000, "opened_date": "1962-01-01"},
        {"id": 3, "name": "Wrigley Field", "team_id": 3, "city": "Chicago", "state": "IL", "capacity": 41649, "opened_date": "1914-01-01"},
    ]

    try:
        for data in data:
            session.execute(
                text("""
                    INSERT INTO mlb.parks (id, name, team_id, city, state, capacity, opened_date)
                    VALUES (:id, :name, :team_id, :city, :state, :capacity, :opened_date)
                    ON CONFLICT (id) DO UPDATE
                    SET name = EXCLUDED.name,
                        team_id = EXCLUDED.team_id,
                        city = EXCLUDED.city,
                        state = EXCLUDED.state,
                        capacity = EXCLUDED.capacity,
                        opened_date = EXCLUDED.opened_date
                """),
                data
            )
        session.commit()
    
    except Exception as e:
        session.rollback()
        print(f"Error during upsert: {e}")