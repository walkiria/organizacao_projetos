import os


def create_folder(path_name):
    try:
        os.mkdir(path+path_name)
    except OSError:
        print ("Creation of the directory %s failed" % path+path_name)
    else:
        print ("Successfully created the directory %s " % path+path_name)


def create_file(content=None, path=None):
    f = open(path, "a")
    f.write(content)
    f.close()


def call_create_folders(project_name):
    subfolders = ['data', 'docs','models', 'notebooks', 'references', 'reports', 'src']
    subfolders_data = ['external', 'interim', 'processed', 'raw']
    subfolders_reports= ['figures']
    subfolders_src = ['data', 'features', 'models', 'visualization']

    create_folder(project_name)
    for i in subfolders:
        create_folder(project_name+i)

    for i in subfolders_data:
        create_folder(project_name+'data'+ '/'+i)

    for i in subfolders_reports:
        create_folder(project_name+'reports'+ '/'+i)

    for i in subfolders_src:
        create_folder(project_name+'src'+ '/'+i)



def call_create_files(path, project_name):
    config = path+project_name+'config.json'
    main = path+project_name+'Main.py' 
    readme= path+project_name+'README.md'
    train =  path+project_name+'src/models/train.py'
    predict = path+project_name+'src/models/predict.py'
    visualize =  path+project_name+'src/visualization/visualize.py'
    make_dataset = path+project_name+'src/data/make_dataset.py'

    files  = [main,config, readme,train, predict, visualize, make_dataset]

    for i in files:
        create_file("",i)

def create_git_folders(project_name):
    call_create_folders(project_name)
    call_create_files(path, project_name)



if __name__  == '__main__':
	path = os.getcwd()
	path = path+'/'
	print('Nome do projeto')
	project_name = input()
	project_name = project_name +'/'

	create_git_folders(project_name)




