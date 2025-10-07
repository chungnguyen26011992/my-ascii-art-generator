from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    if request.method == 'POST':
        text = request.form.get('text')
        font = request.form.get('font', 'slant')
        if text:
            try:
                fig = pyfiglet.Figlet(font=font)
                ascii_art = fig.renderText(text)
            except pyfiglet.FontNotFound:
                # Handle font not found error
                ascii_art = "Font not found!"

    return render_template('index.html', ascii_art=ascii_art)

if __name__ == '__main__':
    app.run(debug=True)
