from sqlalchemy import (
    Column,
    ForeignKey,
    ForeignKeyConstraint,
)
from sqlalchemy.orm import (
    backref,
    relationship,
)
from sqlalchemy.types import (
    Integer,
    Unicode,
)

from pynformatics.model.meta import Base
from pynformatics.utils.functions import attrs_to_dict


class PynformaticsRun(Base):
    __table_args__ = (
        ForeignKeyConstraint(
            ['run_id', 'contest_id'],
            ['ejudge.runs.run_id', 'ejudge.runs.contest_id'],
        ),
        {'schema': 'pynformatics'},
    )
    __tablename__ = 'run'

    run_id = Column('run_id', ForeignKey('ejudge.runs.run_id'), primary_key=True)
    contest_id = Column('contest_id', ForeignKey('ejudge.runs.contest_id'), primary_key=True)
    run = relationship(
        'Run',
        foreign_keys='[PynformaticsRun.run_id, PynformaticsRun.contest_id]',
        backref=backref('pynformatics_run', lazy='joined', uselist=False),
        lazy='joined'
    )

    statement_id = Column(Integer)
    source = Column(Unicode)

    def serialize(self):
        serialized = attrs_to_dict(
            self,
            'statement_id',
            'source'
        )
        return serialized
