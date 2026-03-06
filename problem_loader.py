import json

def load_problems():
    with open("problems.json") as f:
        data = json.load(f)

    all_problems = []

    for group in data["problems"]:
        all_problems.extend(group["problems"])

    return all_problems