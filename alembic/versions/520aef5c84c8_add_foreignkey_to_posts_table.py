"""add foreignkey to posts table

Revision ID: 520aef5c84c8
Revises: a149ddac1f7c
Create Date: 2021-11-05 20:08:27.411442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '520aef5c84c8'
down_revision = 'a149ddac1f7c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
