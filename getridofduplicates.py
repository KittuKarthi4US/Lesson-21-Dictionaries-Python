student_data = {
    "id1": {'name': 'Sara', 'class': 'V', 'subject': 'maths, english, science' },
    "id2": {'name': 'Vihaan', 'class': 'V', 'subject': 'history, english, science' },
    "id3": {'name': 'Sara', 'class': 'V', 'subject': 'maths, english, science' },
    "id4": {'name': 'Ryan', 'class': 'V', 'subject': 'maths, physics, science' }
}

res = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details['name'],details['class'], details['subject'])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        res[student_id] = details

for k, v in res.items():
    print(k , ':' , v)