"""updating i guess

Revision ID: 375b97ec2009
Revises: 2302ca8f41b3
Create Date: 2018-11-07 09:55:05.525362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '375b97ec2009'
down_revision = '2302ca8f41b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_name'), 'admin', ['name'], unique=False)
    op.drop_index('ix_admin_model_name', table_name='admin_model')
    op.drop_table('admin_model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_admin_model_name', 'admin_model', ['name'], unique=False)
    op.drop_index(op.f('ix_admin_name'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###
