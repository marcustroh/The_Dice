import random
def dice(code):
    dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    position_1 = -1
    position_2 = -1
    for i in code:
        position_1 = position_1 + 1
        if i == "D":
            tries = code[:position_1]
            # print(f"tries: {tries}")
            for j in code:
                position_2 = position_2 + 1
                if j == "+":
                    dice_type = code[position_1+1:position_2]
                    dice_type_code = code[position_1:position_2]
                    modifier = code[position_2+1:]
                    # print(f"dice type: {dice_type}")
                    # print(f"dice type code: {dice_type_code}")
                    # print(f"modifier: {modifier}")
                    if dice_type_code in dices:
                        None
                    else:
                        return f"There is no such dice type like {dice_type_code}. Please provide correct one"

    dice_sum = 0
    for k in range(int(tries)):
        dice_result = random.randint(1, int(dice_type))
        dice_sum = dice_sum + dice_result
        # print(f"Dice: {dice_result}")

    # print(f"dice sum: {dice_sum}")
    result = dice_sum + int(modifier)
    return f"Total result: {result}"



print(dice('2D10+10'))
