"""empty message

Revision ID: 3a1e034b3ab8
Revises: bb38bc8648dd
Create Date: 2022-06-11 07:56:03.821014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a1e034b3ab8'
down_revision = 'bb38bc8648dd'
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
    sa.Column('telepon', sa.String(length=20), nullable=False),
    sa.Column('tujuan', sa.String(length=250), nullable=False),
    sa.Column('foto', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guestbook')
    # ### end Alembic commands ###
