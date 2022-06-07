"""empty message

Revision ID: 210d9d5c6f0e
Revises: cc0bee488bfb
Create Date: 2022-06-07 07:23:39.878848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '210d9d5c6f0e'
down_revision = 'cc0bee488bfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guestbook',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.DateTime(), nullable=True),
    sa.Column('nama', sa.String(length=80), nullable=False),
    sa.Column('instansi', sa.String(length=100), nullable=False),
    sa.Column('alamat', sa.String(length=150), nullable=False),
    sa.Column('telepon', sa.Integer(), nullable=False),
    sa.Column('tujuan', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guestbook')
    # ### end Alembic commands ###
