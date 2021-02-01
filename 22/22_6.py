import pickle
my_list = ['1',73,"Hello there",81.21212e-13]
pickle_file = open("my_pickled_list.pkl","w")
pickle.dump(my_list,pickle_file)
pickle_file.close()
