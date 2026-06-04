#Gentry Bayer 
#6/2/2026 
#Medical Data Validator 
import re   # this imports the module 

medical_records = [ #this is the dictionary of the information
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'Female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 29,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]
#this function is finding the invalid records 
def find_invalid_records( 
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
#this is another dictionary, it is named the constraints dictionary. 
    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),

        'age': isinstance(age, int) and age >= 18,
#this is checking if the gender is a string and if the lower case gender is in male or female. 
        'gender': isinstance(gender, str)
        and gender.lower() in ('male', 'female'),
#this is checking if diagnosis is a string and or if it is None 
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
#this is checking if medications is a list and if it is a string 
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
#this is checking if last_visit_id is a string, and if it consists of a V or v followed by one or more digits. 
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }
#this is returning the value 
    return [key for key, value in constraints.items() if not value]

# this is defining a new function and checking if it is a list or tuple. 
def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False
#this is another small dictionary 
    key_set = {
        'patient_id',
        'age',
        'gender',
        'diagnosis',
        'medications',
        'last_visit_id'
    }
#this is a for loop 
    for index, dictionary in enumerate(data):

        if not isinstance(dictionary, dict):
            print(
                f'Invalid format: expected a dictionary at position {index}.'
            )
            is_invalid = True
            continue
#this is an if statement 
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} '
                'has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)

        for key in invalid_records:
            print(
                f"Unexpected format '{key}: {dictionary[key]}' "
                f"at position {index}."
            )
            is_invalid = True

    if is_invalid:
        return False

    print('Valid format.')
    return True


validate(medical_records)