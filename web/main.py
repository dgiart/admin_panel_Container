from app import app
#17.10, 04/10
import view
# from time import time, asctime
# from flask import render_template



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #app.run(port=8000, debug=True)
    app.run(host='0.0.0.0', port = 8080)