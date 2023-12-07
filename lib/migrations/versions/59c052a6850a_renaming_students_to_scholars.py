"""Renaming students to scholars

Revision ID: 59c052a6850a
Revises: 791279dd0760
Create Date: 2023-12-07 21:16:11.605768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59c052a6850a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

    


def downgrade() -> None:
     op.rename_table('scholars', 'students')
  
