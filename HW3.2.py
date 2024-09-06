# START
grades: int = int(input('enter your grade:'))
if 0 <= grades <= 40:
    print('try harder next time...')
elif 41 <= grades <= 60:
    print("you'r getting there, need some more work")
elif 61 <= grades <= 80:
    print("pretty good")
elif 81 <= grades <= 95:
    print('awesome!')
elif 96 <= grades <= 100:
    print("excellent!!!you'r a Star!")
else:
    print('illegal grade')
# END
