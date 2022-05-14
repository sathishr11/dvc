import re
from src.utils.all_utils import create_directory, read_yaml, save_dataframe
import argparse
import pandas as pd
import os
from sklearn.linear_model import ElasticNet
import joblib


def train_model(config_path, params_path):

    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # retrieve the path of the data
    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']
    train_data_file = config['artifacts']['train_file']
    test_data_file = config['artifacts']['test_file']

    train_data_path = os.path.join(artifacts_dir, split_data_dir, train_data_file)
    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_data_file)

    train_data = pd.read_csv(train_data_path)
    test_data = pd.read_csv(test_data_path)

    # split depenedent and independent variables
    X_train = train_data.drop(['quality'], axis=1)
    y_train = train_data['quality']
    X_test = test_data.drop(['quality'], axis=1)
    y_test = test_data['quality']

    # get the parameters from params.yaml
    alpha = params['model_params']['ElasticNet']['alpha']
    l1_ratio = params['model_params']['ElasticNet']['l1_ratio']
    random_state = params['model_params']['ElasticNet']['random_state']

    # train elastic net model    
    elastic_net = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    elastic_net.fit(X_train, y_train)
    print(f'ElasticNet model trained with alpha={alpha}, l1_ratio={l1_ratio}, random_state={random_state}')

    model_dir = config['artifacts']['model_dir']
    model_file = config['artifacts']['model_file']
    model_path = os.path.join(artifacts_dir, model_dir, model_file)

    create_directory([model_dir])

    joblib.dump(elastic_net, model_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    train_model(config_path=parsed_args.config, params_path=parsed_args.params)