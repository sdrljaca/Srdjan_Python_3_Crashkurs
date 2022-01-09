x = 0
y = 0
large_enterprises = ['Raiffeisen Bank', 'A1', 'Erste Bank']
name = "srđan"
surname = "drljača"
full_name = f"{name} {surname}"

experience = ['m:tel', 'IRIS', 'SPL Tele']
experience.insert(1, 'ELNOS') #Ups! Zaboravio sam Elnos
experience[1] = 'ENOS BL' #Ups! Zaboravio sam BL u Elnos

print(f"\tCiao, {full_name.title()}!\n\t---------------------")
print (f"\tHe works by {experience[-1]}, his {len(experience)}. Company")
print (f"\tBefore {experience[-1]} he worked by:")
for company in experience[:-1]:
    x = x + 1
    print(f"\t{x}. {company}")

def compare(experience, large_enterprises):
    for i in experience:
        if i in large_enterprises:
            return True
    return False

if compare(experience, large_enterprises):
    print(f"Bravo {full_name.title()}!!!")
else:
    print("You have to gain experience in Large Enterprise")