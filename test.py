import requests
message_id=15938
rt = requests.get('https://api.vk.com/method/messages.delete?message_ids='+str(message_id)+'&delete_for_all=1&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92')
print(rt.text)