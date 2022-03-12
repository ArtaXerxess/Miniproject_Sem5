import pickle,os

class FileSearchEngine:
    def __init__(self):
        self.file_index = [] 
        self.results = [] 
        self.matches = 0 
        self.records = 0
    def create_new_index(self, root_path):
        self.file_index = [(root,files) for root,dirs,files in os.walk(root_path) if files]
        with open('file_index.pkl','wb') as foo:
            pickle.dump(self.file_index,foo)
            foo.close()
    def load_existing_index(self):
        try:
            with open('file_index.pkl','rb') as foo:
                self.file_index = pickle.load(foo)
                foo.close()
        except:
            self.file_index = []
    def search(self,term,search_type='contains'):
        self.matches = 0
        self.records = 0
        self.results.clear()
        for path, files in self.file_index:
            for file in files:
                self.records += 1
                if (search_type == 'contains' and term.lower() in file.lower() or
                search_type == 'startswith' and file.lower().startswith(term.lower()) or 
                search_type == 'endswith' and file.lower().endswith(term.lower())):
                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue
        with open('search_results.txt','w') as f:
            f.write('name of file:{}\n'.format(term))
            f.write('{} Matches Found!\n'.format(self.matches))
            for row in self.results:
                f.write(row+'\n')
            f.close()

def find_the_file(file_name):
    path = 'C:/Users/WiiN10pro' #C:/Users/WiiN10pro
    print('Finding {}...'.format(file_name))
    Guddu= FileSearchEngine()
    Guddu.create_new_index(path)
    Guddu.search(file_name)
    print("files containing the name {} are found, we have {} matches".format(file_name,Guddu.matches))
    os.remove('file_index.pkl')
    os.startfile('search_results.txt')


find_the_file(str(input("Enter the name of file you want to find: ")))