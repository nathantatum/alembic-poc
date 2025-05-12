from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from teams import seed_teams
from parks import seed_parks

# Database connection string
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

# Create engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def seed_all():
    try:
        print(f'>>> Seeding teams data')
        seed_teams(session)
        print(f'>>> Seeding parks data')
        seed_parks(session)
        session.commit()
        print(">>> Data seeding complete!")
    except Exception as e:
        session.rollback()
        print(f"Error seeding data: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_all()