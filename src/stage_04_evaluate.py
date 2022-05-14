from src.utils.all_utils import create_directory, read_yaml, save_dataframe, save_evaluation_reports
import argparse
import pandas as pd
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

def evaluate_metrics(y_true, y_pred):
    """Evaluate metrics of the model

    Args:
        y_true (dataframe): Actual values of dependent variable
        y_pred (dataframe): Predicted values of dependent variable

    Returns:
        tuple: metrics of the model
    """
    rmse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return rmse, mae, r2

def evaluate_model(config_path, params_path):

    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # retrieve the path of the data
    artifacts_dir = config['artifacts']['artifacts_dir']
    model_dir = config['artifacts']['model_dir']
    model_file = config['artifacts']['model_file']
    model_file_path = os.path.join(artifacts_dir ,model_dir, model_file)

    split_data_dir = config['artifacts']['split_data_dir']
    test_data_file = config['artifacts']['test_file']
    test_data_path = os.path.join(artifacts_dir, split_data_dir,test_data_file)

    ElasticNet = joblib.load(model_file_path)

    test_data = pd.read_csv(test_data_path)

    # split depenedent and independent variables
    X_test = test_data.drop(['quality'], axis=1)
    y_test = test_data['quality']

    y_pred = ElasticNet.predict(X_test)
    rmse, mae, r2 = evaluate_metrics(y_test, y_pred)

    reports_dir = config['artifacts']['reports_dir']
    reports_file = config['artifacts']['reports_file']
    reports_path = os.path.join(artifacts_dir, reports_dir)

    create_directory([reports_path])

    reports_file_path = os.path.join(reports_path, reports_file)
    save_evaluation_reports({'RMSE': rmse, 'MAE': mae, 'R2': r2}, reports_file_path)




if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    evaluate_model(config_path=parsed_args.config, params_path=parsed_args.params)