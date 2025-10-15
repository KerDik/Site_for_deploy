from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Recruto')
    message = request.args.get('message', 'Давай дружить')
    
    greeting = f"Hello {name}! {message}!"
    
    return render_template('index.html', 
                         greeting=greeting,
                         current_name=name,
                         current_message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)