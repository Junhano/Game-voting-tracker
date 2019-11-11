def print_menu():
    print('r is represent, is to showing the vote and people in the list \nan is add name \nas is add score, only 1 score \nass is add scores, parameter is a string \nc is clean, don\'t use it \nfl final list, decide vote \nre is report, report and record into a text file \ninit is to reread the file \nnl is to people are going to vote for \nq is quit\n')
class TrackingVote:
    def __init__(self,file = 'tracking.txt'):
        self.name_dict = dict()
        with open(file, 'r') as f:
            c = f.readlines()
            for i in c:
                if len(i.rstrip('\n').split()) == 2:
                    self.name_dict[i.rstrip('\n').split()[0]] = int(i.rstrip('\n').split()[1])
                else:
                    self.name_dict[i.rstrip('\n').split()[0]] = 0
    def represent(self):
        for k,v in self.name_dict.items():
            print(f'{k} {v}')
    def add_name(self,names):
        for i in names.split(','):
            if i not in self.name_dict.keys():
                self.name_dict[i] = 0  
        self.report()
    
    def add_scores(self,string):
        string = string.replace(' ','').split(',')
        if len(string) <= 20:
            for i in string:
                for k in self.name_dict.keys():
                    if k.upper() == i.upper():
                        self.name_dict[k] += 1
            self.report()
    def add_score(self,name):
        if name in self.name_dict.keys():
            self.name_dict[name] += 1
    def name_list(self):
        return ','.join(list(self.name_dict.keys()))
    def final_list(self):
        return_list = []
        count = 0
        for k,v in sorted(self.name_dict.items(),key = lambda x: x[1], reverse = True):
            if count == 20:
                break
            else:
                return_list.append(k)
                count += 1
        return return_list
    
    def clean(self):
        self.name_dict = dict()
        self.report()
    def report(self,file = 'tracking.txt' ):
        with open(file,'w') as w:
            for k,v in self.name_dict.items():
                w.write(f'{k} {v}\n')
                
if __name__ == '__main__':
    c = TrackingVote()
    print_menu()
    input1 = input('Please enter what you want to choose: ')
    while input1 != 'q':
        if input1 == 'r':
            c.represent()
        elif input1 == 'an':
            input2 = input('Add name, can be a string of name that separate by comma: ')
            c.add_name(input2)
        elif input1 == 'as':
            input2 = input('Add only 1 score: ')
            c.add_score(input2)
        elif input1 == 'ass':
            input2 = input('Please add the string and press enter: ')
            c.add_scores(input2)
        elif input1 == 'c':
            input2 = input('Are you sure? Y/N')
            if input2 == 'Y':
                c.clean()
        elif input1 == 'fl':
            print(c.final_list())
        elif input1 == 'nl':
            print(c.name_list())
        elif input1 == 're':
            c.report()
        elif input1 == 'init':
            c = TrackingVote()
        elif input1 == 'help':
            print_menu()
        input1 = input('please enter what you want to choose: ')