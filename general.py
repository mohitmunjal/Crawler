import os

#Each website you crawl is a seperate project( folder)
#directory is the path to that folter
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)

#Creates queue and crawled files ( if not created)
#create_data_files('Ecounsellors','https://ecounsellors.in/')
def create_data_files(project_name, baseurl):
    queue = project_name + '/queue.txt' #filename ecounsellors/queue.txt
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,baseurl) #initially base url given
    if not os.path.isfile(crawled):
        write_file(crawled,'') #initially crawled file will be empty

#Creates a new file
def write_file(file_name, data):
    f=open(file_name,'w')
    f.write(data)
    f.close()

#Add data to a existing file
def append_to_file(file_name,data):
    with open(file_name,'a') as file:
        file.write(data + '\n')

#Delete the contents of the file
def delete_file_contents(file_name):
    with open(file_name,'w'):
        pass

#Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))#jo humne new line daali thi humein wo nhi chahiye as part of our link
    return results

#Iterate through a set, each item in the set will be a new line in the file
def set_to_file(links_set, file): #links_set will have all the data that is upto date
    delete_file_contents(file)
    for link in sorted(links_set):
        append_to_file(file,link)
