"""New update system

Revision ID: 4465da1dbb37
Revises: 4f3a2b5c6d7e
Create Date: 2025-05-14 10:24:38.261189+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4465da1dbb37'
down_revision = '4f3a2b5c6d7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('system_update', schema=None) as batch_op:
        batch_op.add_column(sa.Column('upd_profile', sa.Text(), nullable=True))
        batch_op.drop_column('upd_train')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('system_update', schema=None) as batch_op:
        batch_op.add_column(sa.Column('upd_train', sa.VARCHAR(length=50), nullable=False))
        batch_op.drop_column('upd_profile')

    # ### end Alembic commands ###
