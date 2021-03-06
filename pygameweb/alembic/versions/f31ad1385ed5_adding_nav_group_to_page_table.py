"""adding nav_group to page table

Revision ID: f31ad1385ed5
Revises: 6cb6a6a151b7
Create Date: 2017-02-24 21:17:38.810973

"""

# revision identifiers, used by Alembic.
revision = 'f31ad1385ed5'
down_revision = '6cb6a6a151b7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page', sa.Column('nav_group', sa.String(length=255), nullable=True))
    op.execute("UPDATE page SET nav_group='Info' where id in (24, 36, 27, 32, 4, 15)")
    op.execute("UPDATE page SET nav_group='Projects' where id in (1, 16, 37)")
    op.execute("UPDATE page SET nav_group='Development' where id in (14, 31)")
    op.execute("UPDATE page SET uri='wiki/FrequentlyAskedQuestions' where id=36")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('page', 'nav_group')
    # ### end Alembic commands ###
