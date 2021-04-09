"""create all tables

Revision ID: 939d5b86a8f3
Revises: 
Create Date: 2021-04-09 09:09:30.690610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '939d5b86a8f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('are')
    op.drop_table('author')
    op.drop_table('publisher')
    op.drop_table('has')
    op.drop_table('category')
    op.drop_table('issues')
    op.drop_table('book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), nullable=True),
    sa.Column('published_date', sa.DATE(), nullable=True),
    sa.Column('publisher_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('issues',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('book_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('start_date', sa.DATE(), nullable=True),
    sa.Column('end_date', sa.DATE(), nullable=True),
    sa.Column('return_date', sa.DATE(), nullable=True),
    sa.Column('did_pay_fine_check', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('end_date >= start_date'),
    sa.CheckConstraint('return_date >= end_date'),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('has',
    sa.Column('author_id', sa.INTEGER(), nullable=False),
    sa.Column('book_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('author_id', 'book_id')
    )
    op.create_table('publisher',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), nullable=True),
    sa.Column('founded_date', sa.DATE(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('author',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), nullable=True),
    sa.Column('gender', sa.VARCHAR(length=1), nullable=True),
    sa.Column('birthday', sa.DATE(), nullable=True),
    sa.Column('nickname', sa.VARCHAR(length=25), nullable=True),
    sa.CheckConstraint("gender = 'M' OR gender = 'F'"),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('are',
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.Column('book_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'book_id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), nullable=True),
    sa.Column('username', sa.VARCHAR(length=16), nullable=True),
    sa.Column('password', sa.VARCHAR(length=16), nullable=True),
    sa.Column('birthday', sa.DATE(), nullable=True),
    sa.Column('card_number', sa.VARCHAR(length=14), nullable=True),
    sa.Column('is_librarian', sa.BOOLEAN(), nullable=True),
    sa.Column('is_admin', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('card_number'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
