"""create posts table

Revision ID: 40ac37c6fb3c
Revises: 
Create Date: 2021-11-05 19:14:56.294827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40ac37c6fb3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
    pass
