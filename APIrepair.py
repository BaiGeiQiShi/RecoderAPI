import _Applier as app
import json
import sys
import os
from Searchnode import Node
from stringfycode import stringfyRoot
import javalang
import subprocess
import time
import signal
import traceback
from sys import argv

def convert_time_to_str(time):
    #时间数字转化成字符串，不够10的前面补个0
    if (time < 10):
        time = '0' + str(time)
    else:
        time=str(time)
    return time

def sec_to_data(y):
    h=int(y//3600 % 24)
    d = int(y // 86400)
    m =int((y % 3600) // 60)
    s = round(y % 60,2)
    h=convert_time_to_str(h)
    m=convert_time_to_str(m)
    s=convert_time_to_str(s)
    d=convert_time_to_str(d)
    # 天 小时 分钟 秒
    return d + ":" + h + ":" + m + ":" + s
def getroottree2(tokens, isex=False):
    root = Node(tokens[0], 0)
    currnode = root
    idx = 1
    for x in tokens[1:]:
        if x != "^":
            nnode = Node(x, idx)
            nnode.father = currnode
            currnode.child.append(nnode)
            currnode = nnode
            idx += 1
        else:
            currnode = currnode.father
    return root
def urepair(savedata,project,bugid):
    starttime = time.time()
    patches = savedata
    curride = ""
    result = []
    for i, p in enumerate(patches):
        endtime = time.time()
        print(str(i))
        if endtime - starttime > 18000:
            open('timeg.txt', 'a').write(xsss + "\t" + sec_to_data(endtime - starttime) + "\n")
            exit(0)
        try:
            root = getroottree2(p['code'].split())
        except:
            #assert(0)
            continue
        mode = p['mode']
        if mode == 1:
            modestr="insert-before:0$"
            print(modestr)
        else:
            #modestr="replace$"
            modestr = 'replace'
            print(modestr)
        #wf.write(modestr)
        precode = p['precode']
        aftercode = p['aftercode']
        oldcode = p['oldcode']
        if '-1' in oldcode:
            continue
        if mode == 1:
            aftercode = oldcode + aftercode
        lines = aftercode.splitlines()
        if 'throw' in lines[0] and mode == 1:
            for s, l in enumerate(lines):
                if 'throw' in l or l.strip() == "}":
                    precode += l + "\n"
                else:
                    break
            aftercode = "\n".join(lines[s:])
        if lines[0].strip() == '}' and mode == 1:
            precode += lines[0] + "\n"
            aftercode = "\n".join(lines[1:])
        #print(aftercode.splitlines()[:10])

        try:
            code = stringfyRoot(root, False, mode)
        except:
            #print(traceback.print_exc())
            continue
        if '<string>' in code:
            if '\'.\'' in oldcode:
                code = code.replace("<string>", '"."')
            elif '\'-\'' in oldcode:
                code = code.replace("<string>", '"-"')
            elif '\"class\"' in oldcode:
                code = code.replace("<string>", '"class"')
            else:
                code = code.replace("<string>", "\"null\"")
        if len(root.child) > 0 and root.child[0].name == 'condition' and mode == 0:
            code = 'if' + code + "{"
        if code == "" and 'for' in oldcode and mode == 0:
            code = oldcode + "if(0!=1)break;"
        lnum = 0
        for l in code.splitlines():
            if l.strip() != "":
                lnum += 1
            else:
                continue
        if mode == 1 and len(precode.splitlines()) > 0 and 'case' in precode.splitlines()[-1]:
            lines = precode.splitlines()
            for i in range(len(lines) - 2, 0, -1):
                if lines[i].strip() == '}':
                    break
            precode = "\n".join(lines[:i])
            aftercode = "\n".join(lines[i:]) + "\n" + aftercode
        if lnum == 1 and 'if' in code and mode == 1:
            if p['isa']:
                code = code.replace("if", 'while')
            #print('ppp', precode.splitlines()[-1])
            if len(precode.splitlines()) > 0 and 'for' in precode.splitlines()[-1]:
                code = code + 'continue;\n}\n'
            else:
                afterlines = aftercode.splitlines()
                lnum = 0
                rnum = 0
                ps = p
                for p, y in enumerate(afterlines):
                    if ps['isa'] and y.strip() != '':
                        aftercode = "\n".join(afterlines[:p + 1] + ['}'] + afterlines[p + 1:])
                        break
                    if '{' in y:
                        lnum += 1
                    if '}' in y:
                        if lnum == 0:
                            aftercode = "\n".join(afterlines[:p] + ['}'] + afterlines[p:])
                            #assert(0)
                            break
                        lnum -= 1
            '''print(code)
            tmpcode = precode + "\n" + code + aftercode
            tokens = javalang.tokenizer.tokenize(tmpcode)
            parser = javalang.parser.Parser(tokens)
        else:
            print(code)
            tmpcode = precode + "\n" + code + aftercode
            tokens = javalang.tokenizer.tokenize(tmpcode)
            parser = javalang.parser.Parser(tokens)
        try:
            tree = parser.parse()
        except:
            #assert(0)
            #print(code)
            #assert(0)
            #print('ttttt')
            continue
        print(filepath2)
        open(filepath2, "w").write(tmpcode)
        bugg = False'''
        if mode == 0:
            #if oldcode.count('\n')!=0:
            modestr += ':0,'+str(oldcode.count('\n')+1)
            modestr += '$' 
        if code == '\n' or code == '' or code == ' ':
            if mode != 1: 
                modestr = 'delete:0,'
                modestr += str(oldcode.count('\n')+1)
        if code.count('{') != 0 and code.count('}') ==0 and mode == 1:
            modestr = 'wrap:0,'
            #if oldcode.count('\n')!=0:
            modestr += str(oldcode.count('\n')+1)
            modestr += '$' 
        print(code)
        code = code.replace('\n', ' ')
        code = modestr + code 
        print(code+'\n-------------\n')
        result.append(code)
        
        des_file = open('patches/%s%s.txt' % (project,bugid), 'at')
        # Write patch to file
        des_file.write(patches[i]["filename"]+","+str(patches[i]["line"])+","+code+"\n")
        des_file.close()

    endtime = time.time()
    print(sec_to_data(endtime - starttime)) 
    sys.stdout = sys.__stdout__

    '''
        #Apply patch
        with open(file_path,'r') as f:
            src = f.readlines()
        pat = pes
        src_app = app.applyPatch(src, pat, lineid)
        out_app = app.toSrc(src_app)
         

        print(pes)

        #Write to file
        des_file = open('patches/%s%s/%d.java' % (project,bugid,patchnum), 'w')
        patchnum = patchnum + 1
        des_file.write(out_app)
        des_file.close() 
        '''
