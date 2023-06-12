

from mainFiles.familyBudget import FamilyBudget

familyBudget = FamilyBudget()

while True:
    input_info = input("Ввод: ")
    if input_info == "0":
        break
    else:
        result = familyBudget.run(1, input_info)
        print(result)
