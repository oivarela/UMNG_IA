from src.models.search_problem import SearchProblemModel
from src.controllers.agent_controller import AgentController

if __name__ == "__main__":
    problem = SearchProblemModel(initial_state=(0, 0), goal_state=(3, 3))
    controller = AgentController(problem)
    controller.run()
