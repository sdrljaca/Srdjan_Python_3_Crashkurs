x = 0
y = 0
z = 0

import comparelists

large_enterprises = ['Raiffeisen Bank', 'A1', 'Erste Bank']
companies = []
hr_0 = {}

hr_0['f_name'] = input("Type your first name: ")
hr_0['l_name'] = input("Type your family name: ")
hr_0['full_name'] = f"{hr_0['f_name']} {hr_0['l_name']}"
print(f"\tCiao, {hr_0['full_name'].title()}!\n\t---------------------")

pooling_active = True
input_company = ""
while pooling_active:
    while input_company != 'q':
        input_company = input("List the companies for which you worked for (write q when you are done): ")
        if input_company != 'q':            #Da bi izbjegli snimanje Q kao kompanije
            companies.append(input_company) #Da bi izbjegli snimanje Q kao kompanije
    hr_0 ['experience'] = companies         #Snimam rezulat u Dictionary
    print (f"\tYuo entered:")
    for company in companies:
        x += 1
        print(f"\t{x}. {company}")
    correct = input("Is this correct or you want to insert/change? [insert/change/yes]: ")
    if correct == 'yes':
        pooling_active = False
    elif correct == "insert":
        x = 0
        input_company = input(f"\tPlease insert company: ")
        input_company_order = int(input(f"\tAt given order: "))-1
        companies.insert(input_company_order,input_company)
    elif correct == "change":
        x = 0
        input_company = input(f"\tPlease correct name of the company: ")
        input_company_order = int(input(f"\tGive order number: "))-1
        companies[input_company_order] = input_company
    else:
        pooling_active = False
print (f"\t{hr_0['full_name'].title()} works by {companies[-1]}, his {len(hr_0['experience'])}. Company")
print (f"\tBefore {hr_0['experience'][-1]}, {hr_0['full_name'].title()} worked by:")
x = 0
for company in companies[:-1]:
    x += 1
    print(f"\t{x}. {company}")

if comparelists.compare(hr_0['experience'], large_enterprises):
    print(f"Bravo {hr_0['full_name'].title()}!!!")
else:
    print("You have to gain experience in Large Enterprise")