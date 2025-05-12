"""create custom schema

Revision ID: a4f76c09c4eb
Revises: 
Create Date: 2025-03-18 21:34:27.682900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4f76c09c4eb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA mlb;")


def downgrade() -> None:
    op.execute("DROP SCHEMA mlb;")
