#coding=utf-8
import logging
import random
import uuid
import time
import base64
import hashlib

#
#高铭 20190206
#
class Funcs:

    @staticmethod
    def print(s):
        #在此控制处理方式
        logging.debug(s)
        print(s)
        return


    @staticmethod
    def md5(s):
        temp = s.encode("utf-8")
        m = hashlib.md5()
        m.update(temp)

        sign = m.hexdigest()
        return sign

    @staticmethod
    def isNoneOrEmpty(s):
        if s==None:return True
        if not s: return True

        try:
            if isinstance(s,str):
                s = s.strip()
                if s == '': return True
        except:
            return  False

        return False

    @staticmethod
    def toInt(s):
        result=0
        try:
            result=float(s)
            result = int(result)
        except:
            result = 0
            pass

        return  result

    @staticmethod
    def toStr(s):
        if s==None:return ""

        try:
            fldtype=type(s).__name__
            if fldtype=='str': return s.strip()
            elif fldtype == 'int' or fldtype == 'float':return str(s)
            elif fldtype=='datetime' or fldtype=='date' or fldtype=='time':
                try:
                    return  s.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    return time.strftime("%Y-%m-%d %H:%M:%S", s)
            elif fldtype=='bool':
                if s==True:
                    return '1'
                else:
                    return '0'
        except:
            return  ""

        return ""


    @staticmethod
    def toSqlStr(s):
        if s==None:return "''"
        if not s: return "''"

        s = s.replace("'", "''")  ##防注入
        return "'"+s+"'"

    @staticmethod
    def timeStr():
        t = time.time()
        it = int(t)
        ts = time.strftime("%Y%m%d%H%M%S", time.localtime(it))  # 14位
        return ts

    @staticmethod
    def guidStr():
        t = time.time()
        it = int(t)
        ms = int(round((t - it) * 1000))
        ts = time.strftime("%Y%m%d%H%M%S", time.localtime(it))  # 14位

        guid = str(uuid.uuid1())
        return  ts + str(ms) + "-" + guid.replace("-", "")

    @staticmethod
    def randStr(len):
        char=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
             ,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
             ,"0","1","2","3","4","5","6","7","8","9"]

        result=""
        i=0
        while i<len:
            randint=random.randint(0,61)
            s=char[randint]
            result+=s
            i+=1

        return result


    @staticmethod
    def base64encode(s):
        s = base64.b64encode(s.encode('utf-8'))
        s = s.decode('utf-8')
        return s

    @staticmethod
    def base64decode(s):
        s=base64.b64decode(s.encode('utf-8'))
        s = s.decode('utf-8')
        return s

if __name__ == '__main__':
    Funcs.print("test")

    s=Funcs.myguid()
    print(s)

