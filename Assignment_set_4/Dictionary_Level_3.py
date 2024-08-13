# Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
# {
# "P":"Pediatrics",
# "O":"Orthopedics",
# "E":"ENT
# } 

# Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.

# Note: 

# Assume that there is always only one medical speciality which is visited by maximum number of patients.

# Perform case sensitive string comparison wherever necessary.

"""
--------------------------------------------------------------------------------------------------------------
        sample Input                                                          Expected Output
---------------------------------------------------------------------------------------------------------------

[101,P,102,O,302,P,305,P]legs-400                          ||                                     Pediatrics
[101,O,102,O,302,P,305,E,401,O,656,O]legs-11               ||                                     Orthopedics
[101,O,102,E,302,P,305,P,401,E,656,O,987,E]legs-12         ||                                       ENT

---------------------------------------------------------------------------------------------------------------
 
  """
  


def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    speciality_count = {}

  
    for i in range(1, len(patient_medical_speciality_list), 2):
        speciality_code = patient_medical_speciality_list[i]
        if speciality_code in speciality_count:
            speciality_count[speciality_code] += 1
        else:
            speciality_count[speciality_code] = 1


    max_speciality_code = max(speciality_count, key=speciality_count.get)
    speciality = medical_speciality.get(max_speciality_code)

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)