"""add content column to posts table

Revision ID: cd431f7e7047
Revises: 880dcdec7288
Create Date: 2021-11-15 15:07:42.520075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd431f7e7047'
down_revision = '880dcdec7288'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
