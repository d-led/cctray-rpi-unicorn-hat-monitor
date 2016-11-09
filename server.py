#!/usr/bin/env python

from flask import Flask
from flask import request
from sink import Sink
from flask.ext.httpauth import HTTPBasicAuth
from matrix import Matrix
import sys

if len(sys.argv) == 0:
    # use Unicorn HAT when started without parameters
    from RealHat import RealHat
    hat = RealHat()
else:
    # just show the matrix status on the console when started with one parameter
    from FakeHat import FakeHat
    hat = FakeHat()

#################################################################################

app = Flask(__name__)
auth = HTTPBasicAuth()

app.debug = True
led = Matrix(hat)
sink = Sink(led)

# http post http://127.0.0.1:5500/update status:='["NONE","BUILDING","OK","ERROR","NONE","WHAT?"]' --auth giveme:someled
# win: http post http://giveme:someled@127.0.0.1:5500/update  status:="[\"NONE\",\"BUILDING\",\"OK\",\"ERROR\",\"NONE\",\"WHAT?\"]"
@app.route("/update",methods=['POST'])
@auth.login_required
def update():
    content = request.get_json(silent=True)
    status = content['status']
    return str(sink.put(status))

@auth.verify_password
def verify_password(username, password):
    return username=='giveme' and password=='someled'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5500)
