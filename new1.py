import json
import requests

'''
masterdata_url = "https://ab-solution-engineer-task.s3.ap-southeast-1.amazonaws.com/list.txt"
response = requests.post(masterdata_url, data=json_object, headers={"Content-Type": "application/json"})
res = response.json()
'''

res = '[{"name":"Revanth","email":"revanthgss@almabase.com","image":"https://ab-solution-engineer-task.s3.ap-southeast-1.amazonaws.com/birthday.gif"},'
res = res + '{"name":"Vaibhav","email":"vaibhav@almabase.com","image": "https://ab-solution-engineer-task.s3.ap-southeast-1.amazonaws.com/birthday2.gif"}]'

master_data = json.loads(res)

for i in range (0, len(master_data)):
    display_name = master_data[i]['name']
    email = master_data[i]['email']
    img = master_data[i]['image']

    myurl = 'http://127.0.0.1:5000/bdaywish'

    response = requests.post(url, data=json_object, headers={"Content-Type": "application/json"})
    data = response.json()

    a_json = json.loads(data)

    print(a_json['data'])
    


















                       
