import random

people = [i + 1 for i in range(22)]

# For keeping track of who has seen whom
seen = {}
for person in people:
    seen[person] = set()


while True:
    weeks = []
    for week in range(7):
        groups = []

        people = [i + 1 for i in range(22)]

        # Sort 20 people into a group
        for i in range(5):
            group = []
            for j in range(4):
                person = people.pop(random.randrange(len(people)))
                group.append(person)
            groups.append(group)

        # Add the 2 stragglers
        while True:
            group_num_1 = random.randrange(5)
            group_num_2 = random.randrange(5)
            if group_num_1 != group_num_2:
                break

        groups[group_num_1].append(people.pop())
        groups[group_num_2].append(people.pop())

        # No one left to sort
        assert len(people) == 0
        
        weeks.append(groups)

        # Note who saw whom this week
        for group in groups:
            for seeing in group:
                for person in group:
                    seen[seeing].add(person)


    seen_counts = [len(s) for s in seen.values()]
    if all([len(s) == 22 for s in seen.values()]):
        break

for index, week in enumerate(weeks):
    print(f"Week {index + 1}:")
    for jndex, group in enumerate(week):
        print(f"\tGroup {jndex + 1}: " + ", ".join([str(g) for g in group]))
