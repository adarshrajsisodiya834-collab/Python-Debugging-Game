class DebugEngine:
    def __init__(self, problems):
        self.problems = problems
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.problems)

    def get_current_problem(self):
        return self.problems[self.current_index]

    def validate_answer(self, user_input):
        problem = self.get_current_problem()
        correct_line = problem["faulty_line"]
        return int(user_input) == correct_line

    def next_problem(self):
        self.current_index += 1