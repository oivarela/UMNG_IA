from src.views.console_view import ConsoleView
from src.models.search_problem import SearchProblemModel

class AgentController:
    def __init__(self, problem_model):
        self.model = problem_model
        self.view = ConsoleView()

    def run(self):
        # 1. Obtiene el estado inicial
        current_state = self.model.initial_state
        
        # 2. Notifica a la vista
        self.view.show_step(0, current_state, "Inicio")
