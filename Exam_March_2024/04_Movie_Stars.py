budget_for_actors = float(input())

while True:
    actor = input()
    if actor == "ACTION":
        break
    if len(actor) <= 15:
        budget_for_actors -= float(input())
    else:
        budget_for_actors *= 0.80

    if budget_for_actors < 0:
        break
if budget_for_actors >= 0:
    print(f"We are left with {budget_for_actors:.2f} USD.")
else:
    print(f"We need {abs(budget_for_actors):.2f} USD for our actors.")
