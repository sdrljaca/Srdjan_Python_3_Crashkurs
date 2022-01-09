company = []
input_company = ""

while input_company != 'Q':
    input_company = input("List the companies for which you worked for (write Q when you are done): ")
    if input_company != 'Q':
       company.append(input_company)

hr_0 = {
    'company': company
}
print(hr_0)
