import vk


token = '7dc95bd97dc95bd97dc95bd9c27dbdf93a77dc97dc95bd92250e8cc4eb8d12533c1fde2'
session = vk.Session(access_token=token)
version = 5.124
api = vk.API(session)

first = input()
first_id = first.split('/')[-1]

second = input()
second_id = second.split('/')[-1]

first_user = api.users.get(user_ids=first_id, v=version)[0]['id']
second_user = api.users.get(user_ids=second_id, v=version)[0]['id']

friends_first = api.friends.get(user_id=first_user, v=version)['items']
friends_second = api.friends.get(user_id=second_user, v=version)['items']
mutual_friends = []
for item in friends_first:
    if item in friends_second:
        mutual_friends.append(item)

friends = api.users.get(user_ids=mutual_friends, v=version)
for friend in friends:
    print(friend['first_name'] + ' ' + friend['last_name'])

