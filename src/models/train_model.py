import warnings
import logging
warnings.filterwarnings('ignore')
from helpers import hand_files
from sklearn.model_selection import train_test_split, KFold, RandomizedSearchCV
from sklearn.pipeline import Pipeline


def __split_data(features, target, test_size=0.20, seed=42):
    return train_test_split (features, target, test_size=test_size, random_state=seed)


def __get_best_train_params(pipelines, params, scoring, x_train, y_train):
    for name, model in pipelines:
        kfold = KFold(n_splits=10, random_state=21)
        grid = RandomizedSearchCV(model, params, n_iter=25, verbose=True, scoring=scoring, cv=kfold, n_jobs=2)
        grid.fit(x_train, y_train)
        hand_files.save_trained_model(model)
        return dict(model_name=name, model=grid.best_estimator_, results=[grid.best_params_, grid.best_params_])


def __train_model():
    pass

def main():
    pass


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
