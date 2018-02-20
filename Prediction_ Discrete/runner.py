
from flask import Flask, request, jsonify, render_template, make_response
app = Flask(__name__)

# app.config['UPLOAD_FOLDER'] = os.path.join('static')
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("data_directory", help="location of the dataset",type=str)
#
# args = parser.parse_args()
from flask import send_file
import os

#
# @app.route('/get_image')
# def get_image():
#     if request.args.get('type') == '1':
#        filename = 'ok.gif'
#     else:
#        filename = 'error.gif'
#     return send_file(filename, mimetype='image/gif')



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tsne")
def tsne():
    return render_template('tsne.html')

@app.route("/attr")
def attr():
    return render_template('attr.html')

@app.route("/featcorr")
def fc():
    return render_template('featcorr.html')

@app.route("/pair")
def pp():
    return render_template('pair.html')




# @app.route("/data_visualize.png")
# def simple():
#     import datetime
#     from io import BytesIO
#     import random
#
#     from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#     from matplotlib.figure import Figure
#     from matplotlib.dates import DateFormatter
#
#     fig = Figure()
#     ax = fig.add_subplot(111)
#     x = []
#     y = []
#     now = datetime.datetime.now()
#     delta = datetime.timedelta(days=1)
#     for i in range(10):
#         x.append(now)
#         now += delta
#         y.append(random.randint(0, 1000))
#     ax.plot_date(x, y, '-')
#     ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
#     fig.autofmt_xdate()
#     canvas = FigureCanvas(fig)
#     png_output = BytesIO()
#     canvas.print_png(png_output)
#     response = make_response(png_output.getvalue())
#     response.headers['Content-Type'] = 'image/png'
#     return response



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)


