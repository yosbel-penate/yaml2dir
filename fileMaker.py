import sys, getopt, os
from yamldirs.filemaker import Filemaker

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def get_full_url(folder_name):
    current_directory = os.getcwd()
    full_url = f"file://{current_directory}/{folder_name}/"
    return full_url

def get_yaml(yaml_file):
    with open(yaml_file) as f:
        data = f.read()
    return data

def main(argv):
    yaml_file = ''
    worker_dir = ''
    try:
        opts, args = getopt.getopt(argv,"hc:d:",["config=","dir="])
    except getopt.GetoptError:
        print ('fileMaker.py -c <yamlconfig> -d <outputdir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('fileMaker.py -c <yamlconfig> -d <outputdir>')
            sys.exit()
        elif opt in ("-c", "--config"):
            yaml_file = arg
        elif opt in ("-d", "--dir"):
            worker_dir = arg

    if not yaml_file:
        yaml_file = 'config.yaml'
    if not worker_dir:
        worker_dir = "working_dir"

    create_folder(worker_dir)
    url = get_full_url(worker_dir)

    print ('Config file is: ', yaml_file)
    print ('Dir is: ', worker_dir)


    Filemaker(worker_dir, get_yaml(yaml_file))
    print("Ok")

if __name__ == "__main__":
    main(sys.argv[1:])

