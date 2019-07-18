#coding=utf-8
import  configparser
import os,sys

from common.myfuncs import Funcs


'''
ini配置文件操作
'''
class Config:
    #path=os.path.realpath(__file__)
    #path=os.path.abspath(__file__)
    #path=os.path.dirname(os.path.realpath(__file__))

    #cf=None

    def __init__(self):
        # self.inifile=os.path.dirname(os.path.realpath(__file__))+"\\..\\cfg.ini"
        self.inifile = os.path.dirname(os.path.realpath(__file__))
        self.inifile = os.path.dirname(self.inifile)
        if self.inifile.find('/') < 0:
            self.inifile = self.inifile + "\\cfg.ini"
        else:
            self.inifile = self.inifile + "/cfg.ini"
        try:
            self.cf = configparser.ConfigParser()  # 读取ini文件,path为要读取的ini文件的路径
            self.cf.read(self.inifile)

            #补充完整ini文件的说明
            self.get("note", "comment", '本节只是配置说明，不启实际作用')
            self.get("note", "encode", 'ini文件编码格式是ansi，编辑以后保存时请注意')
            self.get("note", "vars", '系统变量有：sysid,orgid,guid,timestr,localtime,dbtime')
            self.get("note", "varscript", '系统变量使用格式：{系统变量名}，如{sysid}; sql参数：{序号}，如{0}、{1}')
            self.get("note", "sysid", '系统编码')
            self.get("note", "orgid", '组织机构编码')
            self.get("note", "guid", '自动产生的guid')
            self.get("note", "timestr", '取时间串')
            self.get("note", "localtime", '取时间')
            self.get("note", "dbtime", '取数据库时间')
        except:
            self.cf=None

        return

    def get(self,sect,key,defa=''):
        if not self.cf : return ""
        if Funcs.isNoneOrEmpty(sect):return ""
        if Funcs.isNoneOrEmpty(key):return ""
        if Funcs.isNoneOrEmpty(defa):defa=""

        v=""
        try:
            v=self.cf.get(sect, key)
        except configparser.NoSectionError as e:
            try:
                self.cf.add_section(sect)
                self.cf.set(sect, key,defa)
                self.cf.write(open(self.inifile, "w"))
            except:
                pass
        except configparser.NoOptionError as e:
            try:
                self.cf.set(sect, key,defa)
                self.cf.write(open(self.inifile, "w"))
            except:
                pass
        except:
            pass

        return v

    def getint(self,sect,key,defa=0):
        if not self.cf : return 0
        if Funcs.isNoneOrEmpty(sect):return 0
        if Funcs.isNoneOrEmpty(key):return 0
        if Funcs.isNoneOrEmpty(defa):defa=0

        v=0
        try:
            v=self.cf.getint(sect, key)
        except configparser.NoSectionError as e:
            try:
                self.cf.add_section(sect)
                self.cf.set(sect, key,defa)
                self.cf.write(open(self.inifile, "w"))
            except:
                pass
        except configparser.NoOptionError as e:
            try:
                self.cf.set(sect, key,str(defa))
                self.cf.write(open(self.inifile, "w"))
            except:
                pass
        except:
            pass

        return v

    def set(self,sect,key,v):
        if not self.cf : return

        try:
            self.cf.set(sect, key,v)
            self.cf.write(open(self.inifile, "w"))
        except configparser.NoSectionError as e:
            try:
                self.cf.add_section(sect)
                self.cf.set(sect, key,v)
                self.cf.write(open(self.inifile, "w"))
            except:
                pass
        except configparser.NoOptionError as e:
            try:
                self.cf.set(sect, key,"")
                self.cf.write(open(self.inifile, "w"))
            except:
                pass
        except:
            pass

        return



if __name__ == '__main__':
    cfg=Config()

    tables=cfg.get('conn','host')
    tables=cfg.get('conn','port')
    tables=cfg.get('conn','database')
    tables=cfg.get('conn','user')
    tables=cfg.get('conn','passwd')

    tables=cfg.get('table','tables')
    tables=tables.strip()
    if tables=='':cfg.set('table','tables','tbl1,tbl2,tbl3')
    print(tables)

    tables=tables.split(',')
    for tbl in tables:
        tbl=tbl.strip()
        if tbl=='':continue

        print(tbl)

        feilds = cfg.get(tbl, 'feilds')
        keyfeilds = cfg.get(tbl, 'keyfeilds')
        keyvalues = cfg.get(tbl, 'keyvalues')

        print(feilds)
        print(keyfeilds)
        print(keyvalues)