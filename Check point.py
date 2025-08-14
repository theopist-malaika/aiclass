def judge(points):
    if int(points) < 40:
        return'Passed'
    else:
        return'Failed'

points=input('Enter your points:')
comment=judge(points)
print(f'You have { comment } with { points } points!')