days=["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
    if(d=="wed"):
        continue
    print(d)
print('---')

days=["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
    if(d=="sun"):
        break
    print(d)
