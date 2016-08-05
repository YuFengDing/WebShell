import string,os


def date(line,path):
    if os.system(line) == 0:
        f = os.popen(line)
        text = f.read()
        f.close()
        return text
    else:
        os.system(line + " 2>" + os.getcwd() + "/error/err.txt\n")
        f = open(os.getcwd()+"/error/err.txt","r")
        text = f.read()
        f.close()
        return text

def ifconfig(line,path):
    if os.system(line) == 0:
        f = os.popen(line)
        text = f.read()
        f.close()
        return text
    else:
        os.system(line + " 2>" + os.getcwd() + "/error/err.txt\n")
        f = open(os.getcwd()+"/error/err.txt","r")
        text = f.read()
        f.close()
        return text



def ls(line,path):
    if os.system("cd " + path + "\n" + line) == 0:
        f = os.popen("cd " + path + "\n" + line)
        text = f.read()
        f.close()
        return text
    else:
        os.system("cd " + path + "\n" + line + " 2>" + os.getcwd() + "/error/err.txt\n")
        f = open(os.getcwd()+"/error/err.txt","r")
        text = f.read()
        f.close()
        return text


def rm(line,path):
    if os.system("cd " + path + "\n" + line) == 0:
        return ""
    else:
        os.system("cd " + path + "\n" + line + " 2>" + os.getcwd() + "/error/err.txt\n")
        f = open(os.getcwd()+"/error/err.txt","r")
        text = f.read()
        f.close()
        return text

def cp(line,path):
    if os.system("cd " + path + "\n" + line) == 0:
        return ""
    else:
        os.system("cd " + path + "\n" + line + " 2>" + os.getcwd() + "/error/err.txt\n")
        f = open(os.getcwd()+"/error/err.txt","r")
        text = f.read()
        f.close()
        return text

    

cmd = {"ifconfig":ifconfig,"ls":ls,"rm":rm,"cp":cp,"date":date}

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



def iscmd(key):
    try:
        cmd[key]
    except:
        return False
    return True

def docmd(line,path):
    arr = get_words_array(line)
    if not iscmd(arr[0]):
        return "sh: 1: "+ arr[0] +": not found"

    return cmd[arr[0]](line,path);
        
