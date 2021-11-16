"""add foreign-key to posts table

Revision ID: a3f40f9c4f0d
Revises: bdc4fffa3558
Create Date: 2021-11-15 16:15:55.168904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3f40f9c4f0d'
down_revision = 'bdc4fffa3558'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_posts_users', 
                        source_table='posts', referent_table='users', 
                        local_cols=['owner_id'], remote_cols=['id'], 
                        ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('fk_posts_users', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
