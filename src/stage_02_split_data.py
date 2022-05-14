import re
from src.utils.all_utils import create_directory, read_yaml, save_dataframe
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split


def split_data(config_path, params_path):

    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # retrieve the path of the data
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']
    split_data_dir = config['artifacts']['split_data_dir']
    train_data_file = config['artifacts']['train_file']
    test_data_file = config['artifacts']['test_file']

    create_directory([os.path.join(artifacts_dir, split_data_dir)])

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)

    df = pd.read_csv(raw_local_file_path)
    
    test_size = params['base']['test_size']
    random_state = params['base']['random_state']
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)

    train_file_path = os.path.join(artifacts_dir, split_data_dir, train_data_file)
    test_file_path = os.path.join(artifacts_dir, split_data_dir, test_data_file)
    
    for data, data_path in (train, train_file_path), (test, test_file_path):
        save_dataframe(data, data_path)
        


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    split_data(config_path=parsed_args.config, params_path=parsed_args.params)