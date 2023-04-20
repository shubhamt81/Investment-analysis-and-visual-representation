from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    params={
        'spider_name':'../tryz/tryal',
        'start_requests': True, 
    }
    return "HELLO, WORLD!"

if __name__=="__main__":
    app.run(debug=True)