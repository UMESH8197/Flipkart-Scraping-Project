from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# if you don't want to hit your python programme or method with help of postman , if you would like to send request or like to access method or my python function with help of url or broweser url so
# so in that case how it is going to work or how it is performing you acpplicaton let's try to understand.

@app.route('/', methods=['GET', 'POST']) # To render Homepage, read entire application, help out to call my particular method which i have appended just below the this particular route.

def home_page():
    return render_template('index.html') # HTML  behave like interpreter , it will not execute complete code it will just parse whatever you have written and base on that popluated your pages.


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)

@app.route('/sudh_function')
def url_test1():

    test1 = request.args.get('val1')
    test2 = request.args.get('val2')
    # test3 = test1 + test2

    return '''<h1>my result is : {}</h1>'''.format(test1, test2)

if __name__== '__main__':
    app.run(host="0.0.0.0",port="5000")
