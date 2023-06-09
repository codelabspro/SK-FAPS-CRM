"""Adding TEXT to body field of Post model

Revision ID: 5c6cd274d34a
Revises: cf31bab344d1
Create Date: 2023-04-02 01:08:50.749117

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '5c6cd274d34a'
down_revision = 'cf31bab344d1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'body',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'body',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
