#pickle
import pickle
myl = ['a','b','c','d','e']
f3=open("f3.txt","wb")
pickle.dump(myl,f3)
f3.close()

#unpivkle
pickle_off=open("f3.txt","rb")
e=pickle.load(pickle_off)
print(e)