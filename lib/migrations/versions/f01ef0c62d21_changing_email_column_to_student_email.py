"""Changing email column to student_email

Revision ID: f01ef0c62d21
Revises: b929eed0d188
Create Date: 2023-12-07 21:46:20.603801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f01ef0c62d21'
down_revision = 'b929eed0d188'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.add_column('scholars', sa.Column('school_email', sa.String(length=55), nullable=True))
     op.drop_column('scholars', 'email')
  


def downgrade() -> None:
    op.add_column('scholars', sa.Column('email', sa.VARCHAR(length=55), nullable=True))
    op.drop_column('scholars', 'school_email')
    

    pass
