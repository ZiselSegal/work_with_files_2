import os
#1
def get_requested_lines(file_name,requested_str):
    with open(file_name,'r') as f:
        sorted_lst = []
        for line in f:
            if line.startswith(requested_str):
                line = line.strip()
                sorted_lst.append(line)
        return sorted_lst
# print(get_requested_lines('example.txt',"hello".capitalize()))

#2
def print_file_lines(file_name):
    with open(file_name,'r') as f:
        for line in f:
            line = line.strip()
            print(f'line length: {len(line)} ** {line} **')
# print_file_lines('example.txt')

#3
def check_identical_files(file1_name,file2_name):
   f1 = open(file1_name,'r')
   f2 = open(file2_name,'r')
   if os.path.getsize(file1_name) != os.path.getsize(file2_name):
       return print('files are not identical')
   for line1,line2 in zip(f1,f2):
       if line1 != line2:
           print('files are not identical')
           f1.close
           f2.close
           return
   print('files are identical')
   f1.close
   f2.close
# check_identical_files('example.txt','test.txt')
