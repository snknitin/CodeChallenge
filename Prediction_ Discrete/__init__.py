from flask import Flask,render_template,make_response
app = Flask(__name__)

from train import Solution
import numpy as np
s=Solution()
from pandas.plotting import scatter_matrix
from io import BytesIO

import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from sklearn.manifold import TSNE
import seaborn as sns

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route("/feat_correlation.png")
def fc():
    # Visualising distribution of data

    features = ['CT', 'cell_size', 'cell_shape', 'MA', 'ECS', 'BC', 'normal_nuclei', 'Mitoses']
    plot=sns.pairplot(data=s.dataframe_all,hue='CLASS')
    fig=plot.fig
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


@app.route("/pca.png")
def pca_plot():
    result = s.pca()
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = Axes3D(fig)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(result['PCA0'], result['PCA1'], result['PCA2'],c='skyblue', cmap="Set2_r", s=60)

    # make simple, bare axis lines through space:
    xAxisLine = ((min(result['PCA0']), max(result['PCA0'])), (0, 0), (0, 0))
    ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')
    yAxisLine = ((0, 0), (min(result['PCA1']), max(result['PCA1'])), (0, 0))
    ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')
    zAxisLine = ((0, 0), (0, 0), (min(result['PCA2']), max(result['PCA2'])))
    ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r')

    # label the axes
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")
    ax.set_title("PCA on the data set")
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response




@app.route("/3dscatter.png")
def scatter():
    # Visualising distribution of data
    from mpl_toolkits.mplot3d import Axes3D

    features = ['CT', 'cell_size', 'cell_shape', 'MA', 'ECS', 'BC', 'normal_nuclei', 'Mitoses']
    fig = plt.figure()
    ax = Axes3D(fig)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(s.dataframe_all['CT'], s.dataframe_all['cell_size'], s.dataframe_all['cell_shape'], c='skyblue', s=60)
    ax.view_init(30, 185)

    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response





@app.route("/data_visualize.png")
def tsne():
    tsne = TSNE(n_components=2, random_state=0)
    x_test_2d = tsne.fit_transform(s.X_test)

    # scatter plot the sample points among 5 classes
    markers = ('s', 'd')
    color_map = {0: 'red', 1: 'blue'}
    fig = plt.figure()
    for idx, cl in enumerate(np.unique(s.y_test)):
        plt.scatter(x=x_test_2d[s.y_test == cl, 0], y=x_test_2d[s.y_test == cl, 1], c=color_map[idx], marker=markers[idx],
                    label=cl)
    plt.xlabel('X in t-SNE')
    plt.ylabel('Y in t-SNE')
    plt.legend(loc='upper left')
    plt.title('t-SNE visualization of test data')

    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)