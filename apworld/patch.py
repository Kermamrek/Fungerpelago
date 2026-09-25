import json
import random

# To set the variant ID, we need to go to the start map (Map010.json) and make the event properly set the variables
# The "code" to do this is 122. That is the event code for "control variables"
# The parameters are as follows: [first_var_id, last_var_id, operation, type, value]
# The first and last id will basically be the same, which will be the var we need to change
# operation codes: 0=set, 1=add, 2=subtract, 3=multiply, 4=divide, 5=modulus - we basically only want 0
# type codes: 0=fixed number, 1=value of other var, 2=random range, 3=value of game data, 4=javascript

# Example:
# "code":122,"indent":0,"parameters":[121,121,0,2,1,4]
# [RanLevel1_1, RanLevel1_1, Set, Random Range, start of range 1, end of range 4]

# What we probably want to set it to is this:
# "code":122,"indent":0,"parameters":[121,121,0,0,(result of seeded rand)]
# This changes the random range and makes the var set from 1-4, based on what the seeded rand gives

# ==LIST OF VARIANT VARIABLES THAT RANDOMISE THE GAME==
# 121 - RanLevel1_1 - range of 1 to 4
# 350 - Basement_2_variable - range of 1 to 2
# 122 - RanLevel1_2 - range of 1 to 2
# 123 - RanLevel1_3 - range of 1 to 3
# 126 - RanLevel3 - range of 1 to 2
# 127 - RanLevel4 - range of 1 to 2
# 128 - RanLevel5 - range of 1 to 3
# 133 - RanThicket2 - range of 1 to 2
# 134 - RanThicket3 - range of 1 to 2

# If "Set_D" is ON (still have no idea where this is declared)
# 121 = 4
# 350 = 2
# 128 = 3

# Additionally there are more random variables that affect other things, which can be found in fortress intro.
# Will look into those if they become a problem.

#def patch_variants(world, multiworld, player) -> None:
archipelago_room_seed = 67
random.seed(archipelago_room_seed)
with open("C:/Program Files (x86)/Steam/steamapps/common/Fear & Hunger/www/data/Map010.json") as f:
    variants = [121, 350, 122, 123, 126, 127, 128, 133, 134]
    try:
        map_data = json.load(f)
        # Page 6 of the common event EV001, where all the variables are stored
        map_data_2 = map_data["events"][1]["pages"][5]["list"]
        for e in map_data_2:
            if e["code"] == 122:
                # Check if var is in the variant list
                if e["parameters"][0] in variants:
                    # Exclude the "if Set_D" events, only include the currently randomised ones
                    if e["parameters"][3] == 2:
                        # I know this isn't actually changing anything in map data, just for show right now
                        e["parameters"][3] = 0
                        match e["parameters"][4]:
                            case 121:
                                e["parameters"][4] = random.randint(1, 4)
                            case 123:
                                e["parameters"][4] = random.randint(1, 3)
                            case 128:
                                e["parameters"][4] = random.randint(1, 3)
                            case _:
                                e["parameters"][4] = random.randint(1, 2)

                        print(json.dumps(e["parameters"], indent=4))
    except Exception as e:
        print(f"{e}")
