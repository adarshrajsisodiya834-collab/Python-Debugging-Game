from problem_loader import load_problems
from engine import DebugEngine

def display_code(code_lines):
    for i, line in enumerate(code_lines, start=1):
        print(f"{i}: {line}")

def main():
    problems = load_problems()
    engine = DebugEngine(problems)

    print("=== Python Debugging Training Engine ===\n")

    while engine.has_next():
        problem = engine.get_current_problem()

        print("\nFind the faulty line:\n")
        display_code(problem["code"])

        user_input = input("\nEnter faulty line number: ")

        if engine.validate_answer(user_input):
            print("\n✅ Correct!")
        else:
            print("\n❌ Incorrect.")

        print("Explanation:", problem["explanation"])

        engine.next_problem()

    print("\n🎉 All problems completed!")

if __name__ == "__main__":
    main()