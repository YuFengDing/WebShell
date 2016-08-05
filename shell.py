# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, jsonify, render_template, request
import getpass,socket,os,string,command
app = Flask(__name__)


def is_whitespace(character):
    for i in range(0,len(string.whitespace)):
        if character == string.whitespace[i]:
            return True

    return False

def get_words_array(temptext):
    text = temptext.strip()
    if text == "":
        return []

    text = text + " "
    arr = [];position = 0;flag = False
    for i in range(0, len(text)):
        if is_whitespace(text[i])and (not flag):
            arr.append(text[position:i].strip())
            position = i
            flag = True
        if not is_whitespace(text[i]):
            flag = False

    return arr;




@app.route('/user_and_pcname')
def user_and_pcname():
    return jsonify(result = getpass.getuser() + "@" + socket.gethostname())

@app.route('/cmd')
def cmd():
    if  os.geteuid() == 0:
        isroot = True
    else :
        isroot = False
    line = request.args.get('line',"", type=str).strip()
    path = request.args.get('path',"~", type=str).strip()
    text = ""
    arr  = get_words_array(line)
    try:
        if arr[0] == "cd":
            if os.system("cd " + path + "\n" + line + "\n") == 0:
                f = os.popen("cd " + path + "\n" + line + "\n"  + "pwd")
                path = f.read()[:-1];
                f.close()
                print(path)
                ishome = True
                for i in range(0,len(os.getenv("HOME"))):
                    if path[i] != os.getenv("HOME")[i]:
                        ishome = False
                        break
                if ishome:
                    path = "~" + path[len(os.getenv("HOME")):]
            else:
                os.system("cd " + path + "\n" + line + " 2>" + os.getcwd() + "/error/err.txt\n")
                f = open(os.getcwd()+"/error/err.txt","r")
                temptext = f.read()
                f.close()

                text =  temptext
        else:
            text = command.docmd(line,path)

    except:
        pass

    return jsonify(path = path,Text = text,isroot=isroot)


@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    text_line = request.args.get('text_line', "", type=str)
    return jsonify(result=text_line)


@app.route('/')
def index():
    return render_template('shell.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
