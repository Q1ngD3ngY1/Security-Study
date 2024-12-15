from flask import Flask
from flask import render_template
from flask import request
from flask import render_template_string

app = Flask(__name__)
@app.route('/mumu',methods=['GET', 'POST'])
def test():
    template = '''
        <div class="center-content error">
            <h1>Hello Mumu, Welcome to SSTI</h1>
            <h3>%s</h3>
        </div> 
    ''' %(request.url)

    return render_template_string(template)

if __name__ == '__main__':
    app.debug = True
    app.run()