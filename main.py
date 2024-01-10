from pulp import LpMaximize, LpProblem, LpVariable, LpStatus
import csv

#STAGE1
#Read Files
gear_data = {}
with open('gear.csv') as csv_file:
    gear_reader = csv.reader(csv_file, delimiter=',')
    for row in gear_reader:
        object_name = row[0]
        weight = float(row[1])
        survival_usefulness = int(row[2])
        combat_usefulness = int(row[3])
        gear_item_description = {'Weight' : weight, 'SurvivalUsefulness' : survival_usefulness, 'CombatUsefulness' : combat_usefulness}
        gear_data[object_name] = gear_item_description

sorted_by_weight = sorted(gear_data.items(), key=lambda x: (x[1].get('Weight', 0), x[0]))
sorted_by_weight_only = [(item[0], item[1]['Weight']) for item in sorted_by_weight]

sorted_by_survival_usefulness = sorted(gear_data.items(), key=lambda x: (x[1].get('SurvivalUsefulness', 0), x[0]))
sorted_by_survival_usefulness_only = [(item[0], item[1]['SurvivalUsefulness']) for item in sorted_by_survival_usefulness]

sorted_by_combat_usefulness = sorted(gear_data.items(), key=lambda x: (x[1].get('CombatUsefulness', 0), x[0]))
sorted_by_combat_usefulnes_only = [(item[0], item[1]['CombatUsefulness']) for item in sorted_by_combat_usefulness]




#STAGE 2
weight_limit = 8
#making model
model = LpProblem(name="model", sense=LpMaximize)

#making variables
knife = LpVariable(name="knife", lowBound=0, upBound=1, cat="Binary")
twoByFour = LpVariable(name="twoByFour", lowBound=0, upBound=1, cat="Binary")
jacket = LpVariable(name="jacket", lowBound=0, upBound=1, cat="Binary")
armor = LpVariable(name="armor", lowBound=0, upBound=1, cat="Binary")
matches = LpVariable(name="matches", lowBound=0, upBound=1, cat="Binary")

#add constraint
model += (2*knife + 3*twoByFour + 3*jacket + 5*armor + 0.5*matches <= weight_limit, "constraint")

#add objective
obj_func = 9*knife + 10*twoByFour + 8*jacket + 8*armor + 4*matches
model += obj_func

#solving
status = model.solve()

#printing outputs
print(f"status: {model.status}, {LpStatus[model.status]}")
