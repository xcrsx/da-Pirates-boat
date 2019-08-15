"""empty message

Revision ID: c540929b3583
Revises: 8f78eb618a35
Create Date: 2019-04-21 19:46:17.512089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c540929b3583'
down_revision = '8f78eb618a35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sound_cloud', sa.Column('date_entry', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sound_cloud', 'date_entry')
    # ### end Alembic commands ###