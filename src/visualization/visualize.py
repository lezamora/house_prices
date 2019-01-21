import os
import seaborn as sns
import matplotlib.pyplot as plt


def plot_check_outliers_box_plot(df, columns_list, figure_path):
    """ Plotea diagramas de caja por cada columna del dataset.

    :param df: Dataframe que se está utilizando para modelar.
    :param columns_list: Columnas que se quieren incluir en el gráfico.
    :param figure_path: Directorio en donde se guardaran las figuras.
    """

    number_of_columns = len(columns_list)
    number_of_rows = number_of_columns-1/number_of_columns
    plt.figure(figsize=(len(columns_list), 5 * number_of_rows))
    for i in range(0, len(columns_list)):
        plt.subplot(number_of_rows + 1, number_of_columns, i + 1)
        sns.set_style('whitegrid')
        sns.boxplot(df[columns_list[i]], color='green', orient='v')
        plt.tight_layout()
        if not os.path.exists(figure_path):
            plt.savefig(figure_path)


def plot_check_correlation(df, k, target, figure_path):
    """ Plotea un mapa de calor para observar la correlación de los features y el target indicado.

        :param df: Dataframe que se está utilizando para modelar.
        :param k: Cantidad de columnas del mapa de calor. Se visualizarán las k mas correlacionadas con el target.
        :param figure_path: Directorio en donde se guardaran las figuras.
        """

    # k: number of variables for heatmap
    cols = df.corr().nlargest(k, target)[target].index
    cm = df[cols].corr()
    plt.figure(figsize=(15, 10))
    sns.heatmap(cm, annot=True, cmap='viridis')
    if not os.path.exists(figure_path):
        plt.savefig(figure_path)


def plot_check_distribution(df, columns_list, figure_path):
    """ Plotea diagramas de distribución por cada cada columna del dataset.

    :param df: Dataframe que se está utilizando para modelar.
    :param columns_list: Columnas que se quieren incluir en el gráfico.
    :param figure_path: Directorio en donde se guardaran las figuras.
    """

    number_of_columns = len(columns_list)
    number_of_rows = number_of_columns - 1 / number_of_columns
    plt.figure(figsize=(2 * number_of_columns, 5 * number_of_rows))
    for i in range(0, len(columns_list)):
        plt.subplot(number_of_rows + 1, number_of_columns, i + 1)
        sns.distplot(df[columns_list[i]], kde=False)
        if not os.path.exists(figure_path):
            plt.savefig(figure_path)
