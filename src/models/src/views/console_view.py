class ConsoleView:
    @staticmethod
    def show_step(step, state, action):
        print(f"[Paso {step}] Estado actual: {state} | Acción: {action}")

    @staticmethod
    def show_solution(path, cost):
        print("\n--- Solución Encontrada ---")
        print(f"Ruta: {path}")
        print(f"Costo total: {cost}")
