# Step 1
# In this workshop, you'll validate a set of medical data to ensure that it complies with a set of rules.
#
# Declare a variable named medical_records and assign it an empty list. In the following steps, you are going to use it to store your medical data.

# Step 2
# As you learned in previous lessons, a dictionary stores key-value pairs. Each key must be unique within the dictionary. Strings are commonly used as keys:

# Example Code
# person = {
    # 'name': 'John',
    # 'age': 33
# }
# ?The medical_records list will store dictionaries, each of them representing a patient. Add a dictionary with a key patient_id and value of the string P1001 to the medical_records list.

# Step 3
# Add a key age with the value of the integer 34 and a key gender with the value of the string Female to your dictionary. Don't forget the comma between the key-value pairs.

medical_records = [
    {
           'patient_id': 'P1001',
           "age": 34,
            "gender":"Female"
       }
]
print("medical records:", medical_records)
