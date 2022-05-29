"""empty message

Revision ID: d0d07ceefae3
Revises: 202bff3e4c99
Create Date: 2022-05-29 11:39:43.730747

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd0d07ceefae3'
down_revision = '202bff3e4c99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('l_b3', 'konversi')
    op.drop_column('l_b3', 'nilai')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('l_b3', sa.Column('nilai', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('l_b3', sa.Column('konversi', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
