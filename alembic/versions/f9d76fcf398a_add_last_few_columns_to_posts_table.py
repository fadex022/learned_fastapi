"""add last few columns to posts table

Revision ID: f9d76fcf398a
Revises: 520aef5c84c8
Create Date: 2021-11-05 20:22:32.643219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9d76fcf398a'
down_revision = '520aef5c84c8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
