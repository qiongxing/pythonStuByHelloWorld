import pickle
pickle_file = open('my_pickled_list.pkl','r')
recover_list=pickle.load(pickle_file)
pickle_file.close()

print recover_list