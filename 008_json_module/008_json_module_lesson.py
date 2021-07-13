import json

# json_string = '''
# {
#     "people": [
#                     {
#                         "name": "Jack Summers",
#                         "phone": "555-555-555",
#                         "emails": ["jack.sumers@example.com", "jacksumers@workplace.com"],
#                         "has_license": false
#                     },
#                     {
#                         "name": "Mary Smith",
#                         "phone": "777-777-777",
#                         "emails": null,
#                         "has_license": true
#                     }
#             ]
# }
# '''

# structured_data = json.loads(json_string)
# # print(structured_data)
# # print(type(structured_data))
# people = structured_data['people']
# # print(people)
# for person in people:
#     print(f"The name is {person['name']}, and phone number is {person['phone']}")
# new_json = json.dumps(structured_data)
# print(new_json)

with open('sample.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)
    people = data['people']
    for person in people:
        if person['has_license'] == False:
            del person['has_license']

with open('sample_log.json', 'w', encoding='utf8') as json_wfile:
    json.dump(data, json_wfile)