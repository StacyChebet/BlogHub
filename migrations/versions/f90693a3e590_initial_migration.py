"""Initial Migration

Revision ID: f90693a3e590
Revises: deef51e5e2bf
Create Date: 2018-11-26 06:21:12.099126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f90693a3e590'
down_revision = 'deef51e5e2bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_hash', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_hash')
    # ### end Alembic commands ###