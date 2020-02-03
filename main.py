from flask import Flask, send_file, render_template, request
import requests
from bs4 import BeautifulSoup
from pyecharts import options as opts
from pyecharts.charts import Map
from PIL import Image

app = Flask(__name__)


def get_data():
    page = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', id="table3")
    rows = table.findAll('tr')
    val = []
    name = []
    for row in rows[1:]:
        num_cunt = row.findAll('td')
        val.append(int(num_cunt[1].text.strip().replace(',', '')))
        this_name = num_cunt[0].text.strip()
        if this_name == 'U.S.':
            name.append('United States')
        else:
            name.append(this_name)

    return name, val


def map_visualmap(name, val):
    c = (
        Map()
        .add("Reported Case", [list(z) for z in zip(name, val)], "world")
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Coronavirus total reported insident: " + str(sum(val))),
            visualmap_opts=opts.VisualMapOpts(
                max_=max(val), is_piecewise=False),

        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    )
    return c
# map_visualmap().render(path = "heatmap.html")


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    name, val = get_data()
    map_visualmap(name, val).render('/tmp/heatmap.html')
    return send_file('/tmp/heatmap.html', attachment_filename='heatmap.htm')


@app.route('/upload')
def upload():
    return render_template("file_upload.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename == '':
            return render_template("file_upload.html")
        f.save('/tmp/' + f.filename)
        img = Image.open('/tmp/' + f.filename).convert('L')
        img.save('/tmp/' + f.filename)
        return send_file('/tmp/' + f.filename, attachment_filename=f.filename)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
