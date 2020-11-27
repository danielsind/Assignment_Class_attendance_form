data = data2 = ""
with open ('CSC_217_attendance_ week1_30.txt') as fp:
    data = fp.read()
with open('CSC_217_attendance_ week1_end.txt') as fp:
    data2 = fp.read()
data +="\n"
data += data2 

with open ('newMergedFile.txt', 'w') as fp:
    fp.write(data) 
with open ('newMergedFile.txt') as names:
    no_repeated_names = set(names.readlines())
    with open('new_list_no_duplicates.txt', 'w') as rmdup:
        rmdup.writelines(set(no_repeated_names))