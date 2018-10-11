from cruds.models import Question
from table import Table
from table.columns import Column

class QuestionTable(Table):
    id = Column(field='id', header="ID")
    text = Column(field='text', header="Question")
    answer = Column(field='answer', header="Answer")
