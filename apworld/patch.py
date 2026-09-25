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
