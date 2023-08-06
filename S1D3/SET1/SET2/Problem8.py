employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

e_date={};

for x in range(0,len(employees)):
    e_date[employees[x]]=defaults;

print(e_date);