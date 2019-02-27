# mylist = {'mydict': [{'A': 'Letter A'}, {'B': 'Letter C'}, {'C': 'Letter C'}]}
# newDict={}
# print(mylist['mydict'])
# for item in mylist['mydict']:
#     newDict.update(item)
    # print(item)

# print(newDict)
# mylist['mydict']=newDict
# print(mylist['mydict']['A'])
from datetime import datetime
# import datetime
# now = datetime.datetime.now()
#
# print(type(now.month))
# print(now.month)
from util.helper import construct_response_message


mylist = {"notes": [{"created_by": "praveen", "content": "trying to put db commands in models.py", "created_at": "2019-01-23 09:44:47.364633", "is_active": True}, {"created_by": "praveen", "content": "trying to put db commands in models.py", "created_at": "2019-01-23 07:54:06.274603", "is_active": True}, {"created_by": "praveen", "content": "trying to put db commands in models.py", "created_at": "2019-01-23 09:45:31.807266", "is_active": True}, {"created_by": "praveen", "content": "trying to put db commands in models.py", "created_at": "2019-01-23 09:44:48.163792", "is_active": True}, {"created_by": "praveen", "content": "langularo", "created_at": "2019-01-28 18:07:08.873088", "is_active": True}, {"created_by": "praveen", "content": "langularo", "created_at": "2019-01-28 18:36:26.576958", "is_active": True}, {"created_by": "praveen", "content": "langularo", "created_at": "2019-01-28 18:36:28.800891", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:37:50.863480", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:40:31.344402", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:41:31.616961", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:42:02.508914", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:42:40.545700", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:42:57.672242", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:45:33.674466", "is_active": True}, {"created_by": "praveen", "content": "check", "created_at": "2019-01-28 18:45:44.427947", "is_active": True}, {"created_by": "praveen", "content": "hi", "created_at": "2019-01-29 01:42:45.577317", "is_active": True}, {"created_by": "nishalini", "content": "hi test check", "created_at": "2019-01-29 05:06:07.820180", "is_active": True}, {"created_by": "Tryin Lanister", "content": "trying to put db commands in models.py", "created_at": "2019-01-29 10:01:01.583896", "is_active": False}, {"created_by": "Tryin Lanister", "content": "trying to put db commands in models.py", "created_at": "2019-01-31 08:43:55.293163", "is_active": True}, {"created_by": "Tryin Lanister", "content": "trying to put db commands in models.py", "created_at": "2019-01-31 12:26:09.785613", "is_active": True}, {"created_by": "Tryin Lanister", "content": "trying to put db commands in models.py", "created_at": "2019-01-31 12:51:56.860116", "is_active": True}, {"created_by": "Lanister", "content": "trying to put db commands in models.py", "created_at": "2019-01-31 14:40:36.628970", "is_active": True}, {"created_by": "starks", "content": "North Remembers", "created_at": "2019-02-01 07:38:37.464906", "is_active": True}, {"created_by": "starks", "content": "North Remembers", "created_at": "2019-02-02 09:31:32.202175", "is_active": True}, {"created_by": "starks", "content": "North Remembers", "created_at": "2019-02-02 09:33:23.093751", "is_active": True}, {"created_by": "praveen", "content": "chumma check pannuvomaeee", "created_at": "2019-02-11 08:06:40.758870", "is_active": True}, {"created_by": "starks", "content": "North Remember", "created_at": "2019-01-23 09:44:44.588639", "is_active": False}, {"created_by": "praveen", "content": "trying to put db commands in models.py", "created_at": "2019-01-23 09:44:46.931591", "is_active": False}]}

newDict=mylist['notes']
list_date=[]

for item in newDict:
    str_date = item['created_at']
    date_date = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S.%f")
    list_date.append(date_date.month)
ste_list=set(list_date)
print(ste_list)
print(list_date)
count_list = {}
for i in ste_list:
    count_list.update({i: list_date.count(i)})

print(count_list)

