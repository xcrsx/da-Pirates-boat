"""popular

Revision ID: 3e7c56757ea4
Revises: 5030d4f29970
Create Date: 2019-03-25 10:11:57.708580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e7c56757ea4'
down_revision = '5030d4f29970'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('popular',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('pic', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('popular')
    # ### end Alembic commands ###
