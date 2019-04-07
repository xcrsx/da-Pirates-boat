"""popular

Revision ID: 1b31cd402566
Revises: 8bd5cd887a51
Create Date: 2019-03-30 23:41:39.626371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b31cd402566'
down_revision = '8bd5cd887a51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_popular_timestamp'), 'popular', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_popular_timestamp'), table_name='popular')
    # ### end Alembic commands ###
