digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

transform_dict = {}

for x in range(len(digits)):
    transform_dict[x+1] = {'French': fr[x], 'English': en[x]}

print(transform_dict)