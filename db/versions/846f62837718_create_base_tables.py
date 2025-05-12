"""create base tables

Revision ID: 846f62837718
Revises: a4f76c09c4eb
Create Date: 2025-03-18 22:10:20.305286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '846f62837718'
down_revision: Union[str, None] = 'a4f76c09c4eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('abbreviation', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('founded_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='mlb'
    )
    op.create_table('parks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('opened_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['mlb.teams.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='mlb'
    )


def downgrade() -> None:
    op.drop_table('parks', schema='mlb')
    op.drop_table('teams', schema='mlb')
