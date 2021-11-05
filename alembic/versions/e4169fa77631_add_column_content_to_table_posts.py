"""add column content to table posts

Revision ID: e4169fa77631
Revises: 40ac37c6fb3c
Create Date: 2021-11-05 19:40:58.867570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4169fa77631'
down_revision = '40ac37c6fb3c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
