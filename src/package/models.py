from functools import partial

from sqlalchemy import Column as Col


Column = partial(Col, nullable=False)
