import datetime,pickle
import os

first_time =True
if os.path.isfile("last_run.pkl"):
    pickle_file = open("last_run.pkl","r")
    last_time = pickle.load(pickle_file)
    pickle_file.close()
    print "The last time this progame was run was ",last_time
    first_time = False

pickle_file = open("last_run.pkl","w")
pickle.dump(datetime.datetime.now(),pickle_file)
pickle_file.close()
if first_time:
    print "Created now pickle file"
