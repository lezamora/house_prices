import sys
sys.path.insert(0, './src')
import os
import logging
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split, KFold, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from helpers import hand_files, constans
from logging.config import fileConfig


def __split_data(features, target, test_size=0.20, seed=42):
    return train_test_split(features, target, test_size=test_size, random_state=seed)


def __train_model(model, name, model_path, params, scoring, x_train, y_train, logger=None):
    kfold = KFold(n_splits=10, random_state=21)
    grid = RandomizedSearchCV(model, params, n_iter=25, verbose=True, scoring=scoring, cv=kfold, n_jobs=1)
    grid.fit(x_train, y_train)
    hand_files.save_trained_model(grid.best_estimator_, model_path, name)
    logger.info('Model name: {} Scoring: {}' 'Best params: {}'.format(name, grid.best_score_, grid.best_params_))


def main(input_file_path, output_model_path):
    logger = logging.getLogger(__name__)

    # cargamos el dataset y definimos los features y nuestro target
    df = hand_files.load_data(input_file_path, 'csv')
    x = df.drop(constans.TARGET, axis=1)
    y = df[constans.TARGET]
    x_train, x_test, y_train, y_test = __split_data(x, y, test_size=0.20, seed=42)

    # instanciamos el modelo que mejor nos dió en los análisis previo y entrenamos
    model = Pipeline([('sts', StandardScaler()),
                      ('xgb', XGBRegressor())])
    logger.info('Entrenando el modelo.')

    __train_model(model, 'xbregresor', output_model_path, constans.GRID_PARAMS, 'r2', x_train, y_train, logger)
    logger.info('Modelo entrenado y guardado en {}'.format(output_model_path))


if __name__ == '__main__':
    logging.config.fileConfig(constans.LOGGIN_PATH)

    processed_data_path = os.path.join(constans.OUTPUT_DATA_PROCESS_PATH, 'kc_house_data_clean_with_outliers.csv')
    main(processed_data_path, constans.OUTPUT_MODEL_PATH)
