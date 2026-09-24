class SearchProblemModel:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        # Define las acciones posibles desde un estado
        return ['UP', 'DOWN', 'LEFT', 'RIGHT']

    def result(self, state, action):
        # Define la transición de estados
        pass
