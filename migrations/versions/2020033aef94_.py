"""empty message

Revision ID: 2020033aef94
Revises: 6bd9af140db6
Create Date: 2021-08-29 12:05:15.304732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2020033aef94'
down_revision = '6bd9af140db6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite', sa.Column('people_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'favorite', 'people', ['people_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorite', type_='foreignkey')
    op.drop_column('favorite', 'people_id')
    # ### end Alembic commands ###
