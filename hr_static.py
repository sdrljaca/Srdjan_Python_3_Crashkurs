x = 0
y = 0

def compare(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

large_enterprises = ['Raiffeisen Bank', 'A1', 'Erste Bank']
hr_0 = {
    'name': 'srđan',
    'surname': 'drljača',
}
hr_0['full_name'] = hr_0['name'] + " " + hr_0['surname']

hr_0['experience'] = ['m:tel', 'IRIS', 'A1', 'SPL Tele']

hr_0['experience'].insert(1, 'ELNOS') #Ups! Zaboravio sam Elnos
hr_0['experience'][1]= 'ENOS BL' #Ups! Zaboravio sam BL u Elnos
print(hr_0)

print(f"\tCiao, {hr_0['full_name'].title()}!\n\t---------------------")
print (f"\tHe works by {hr_0['experience'][-1]}, his {len(hr_0['experience'])}. Company")
print (f"\tBefore {hr_0['experience'][-1]} he worked by:")
for company in hr_0['experience'][:-1]:
    x += 1
    print(f"\t{x}. {company}")

if compare(hr_0['experience'], large_enterprises):
    print(f"Bravo {hr_0['full_name'].title()}!!!")
else:
    print("You have to gain experience in Large Enterprise")