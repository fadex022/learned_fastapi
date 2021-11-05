"""create table user

Revision ID: a149ddac1f7c
Revises: e4169fa77631
Create Date: 2021-11-05 19:58:09.657779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a149ddac1f7c'
down_revision = 'e4169fa77631'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table('users')
    pass
