"""empty message

Revision ID: 65a2b3e99b30
Revises: a1a85f56cd41
Create Date: 2019-04-17 16:53:03.093993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65a2b3e99b30'
down_revision = 'a1a85f56cd41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bandcamp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('art', sa.String(), nullable=True),
    sa.Column('album', sa.String(), nullable=True),
    sa.Column('autor', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bandcamp')
    # ### end Alembic commands ###