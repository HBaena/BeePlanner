import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 



engine = create_engine('mysql://root:123@localhost/BeePlannerDB') # Another method to get info from DB. I rather this one above yours.




conn = engine.connect()

user_id_input = raw_input() #You get the Id from FrontEnd

#	#1
#	When u want to acces an User u get the user and passw then u compare the input

result = conn.execute('SELECT name, password FROM User WHERE user_id = {}'.format(user_id_input)) # Send the id

for row in result:
	user = row['name']
	password = row['password']

print user, password


conn.close()


#	#2
#  Requesting the activitys from a user id

result = conn.execute('SELECT a.name, a.priority, a.finish_time FROM Activity a, User u WHERE a.user_id = u.user_id AND u.user_id = {}'.format(user_id_input))

for row in result:
	activity_name = row['a.name']


# #3
# Requesting task from an activity id