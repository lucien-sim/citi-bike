import pickle

def save_pkl(name,obj):
    with open(name, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_pkl(name):
    with open(name, 'rb') as handle:
        return pickle.load(handle)