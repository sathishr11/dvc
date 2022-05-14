import yaml
import os
import json

def read_yaml(path_to_yaml: str)-> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_directory(dirs:list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f'Directory {dir_path} created')

def save_dataframe(data, data_path, index=False):
    """Save the dataframe to a csv file

    Args:
        data (pandas dataframe): dataframe that needs to be saved
        data_path (string): directory where the dataframe needs to be saved
        index (bool, optional): index parameter for to_csv. Defaults to False.
    """
    data.to_csv(data_path, index=index)
    print(f'Data saved to {data_path}')

def save_evaluation_reports(reports: dict, reports_path: str):
    """Save the evaluation reports to a csv file

    Args:
        reports (dict): dictionary of evaluation reports
        reports_path (string): directory where the evaluation reports needs to be saved
    """
    with open(reports_path, 'w') as f:
        # for key, value in reports.items():
        #     f.write(f'{key}: {value}\n')
        json.dump(reports, f, indent=4)
    print(f'Evaluation reports saved to {reports_path}')