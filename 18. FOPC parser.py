facts = {("R", "apple", "banana"), ("R", "banana", "cherry"), ("R", "apple", "cherry")}
expressions = ["R(apple, banana)", "R(banana, cherry)", "R(apple, cherry)", "R(pear, orange)"]
for expression in expressions:
    predicate, args = expression.split('(')
    args = args.rstrip(')').split(',')
    if (predicate, args[0], args[1]) in facts:
        result = True
    else:
        result = False
    print(f"{expression}: {result}")
