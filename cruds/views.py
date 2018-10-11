from cruds.models import KnowledgeBase
from cruds.tables import QuestionTable
from cruds_adminlte.crud import CRUDView


class KnowledgeBaseView(CRUDView):
    model = KnowledgeBase
    check_login = False
    check_perms = False
    def get_detail_view(self):
        View = super(KnowledgeBaseView, self).get_detail_view()
        class KnowledgeBaseDetailView(View):
            def question_table(self):
                knowledge_base = self.object
                return QuestionTable(knowledge_base.question_set.all())
            def get_context_data(self, **kwargs):
                context = super(KnowledgeBaseDetailView, self).get_context_data()
                context['question_table'] = self.question_table()
                return context
        return KnowledgeBaseDetailView
