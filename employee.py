employees=[]

def add_employee(name , email, address):
    employees.append({"name":name, "email":email, "address":address})
    
def view_employee():
    for employee in employees:
        print(employee["name"],employee["email"],employee["address"])
        
add_employee("abdo","abdo@gamil.com","uganda")

view_employee()