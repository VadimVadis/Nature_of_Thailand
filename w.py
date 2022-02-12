from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                 <html lang="en">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{url_for('static', filename='css/bootstrap.min.css')}">
        <script src="{url_for('static', filename='js/jquery.min.js')}"></script>
        <script src="{url_for('static', filename='js/bootstrap.min.js')}"></script>
        <title>Природа Таиланда</title>
    </head>
    <body>
        <div class="container">
            <h1 align="center">Природа Таиланда</h1>
            <div id="myCarousel" class="carousel slide">
                <ol class="carousel-indicators">
                    <li data-target="#myCarousel" data-slide-to="0"></li>
                    <li data-target="#myCarousel" data-slide-to="1" class="active"></li>
                    <li data-target="#myCarousel" data-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="item">
                        <img src="{url_for('static', filename='img/1.jpg')}" style="width:100%;height:800px;">
                    </div>
                    <div class="item active">
                        <img src="{url_for('static', filename='img/2.jpg')}" style="width:100%;height:800px;">
                    </div>
                    <div class="item">
                        <img src="{url_for('static', filename='img/3.jpg')}" style="width:100%;height:800px;">
                    </div>
                </div>
                <a class="left carousel-control" href="#myCarousel" data-slide="prev">
                    <span class="fa fa-chevron-left fa-lg" style="margin-top:400px"></span>
                </a>
                <a class="right carousel-control" href="#myCarousel" data-slide="next">
                    <span class="fa fa-chevron-right fa-lg" style="margin-top:400px"></span>
                </a>
            </div>
        </div>
    </body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
