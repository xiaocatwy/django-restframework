#coding=utf-8
from common.cfg import Config
from common.myfuncs import Funcs
from common.myproxy import Proxy
import requests

'''
door定位客户端接口
'''
class Client:
    device='door' #设备类型
    token='...' #暂略

    apiver = "1.2.0"

    #认证参数
    username = "admin"
    passwordMD5 = "21232f297a57a5a743894a0e4a801fc3"

    doorUrl="http://192.168.0.158"
    subUrl="/access/sdk.php"
    loginPath="/access/sdk.php/"

    #user_name: '', // 用户验证, md5加密, 默认为tengape
    #password: '', // 密码验证, md5加密, 默认为123456

    def __init__(self,doorUrl,username,password):
        self.cfg = Config()
        self.url = self.cfg.get('main', 'url') + "/device"

        self.doorUrl=doorUrl
        #self.username=username
        self.username=Funcs.md5(username)
        self.passwordMD5=Funcs.md5(password)

    '''
    def login(self,username,password):
        data = {}
        data["username"] = username
        data["password"] = Funcs.md5(password)
        data["http_api_version"] = self.apiver

        myProxy = Proxy(self.loginUrl)
        result = myProxy.postEx(data)
        print(result)
    '''

    def get_heart(self,area_name ): #心调包
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Heart/get_heart"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["area_name"]=area_name #工区标识名称

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如

    '''
    {	
				user_name:'',//用户验证,md5加密,默认为tengape
				password:'', //密码验证 ,md5加密,默认为123456
				theid:'',//部门唯一ID
				area_name: 'yeguoxiong', //区域名称
				number:'2',//部门编号
				department:'',//部门
				group_name:'',//部门名称
				remarks:'',//部门备注
			}
	'''
    def add_group(self,theid,area_name,number,department,group_name,remarks ): #添加班组
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Group/add_group"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid
        data["area_name"]=area_name
        data["number"]=number
        data["department"]=department
        data["group_name"]=group_name
        data["remarks"]=remarks

        result=Proxy.send(self.url,data)
        return result #异常返回值为''


    '''
    {
				theid:'' //班组唯一码
				area_name:'yeguoxiong', //区域名称
				number:'2',//部门编号
				department:'腾猿科技',//部门
				group_name:'开挖班组',//部门名称
				remarks:'',//部门备注
			}
	'''
    def edit_group(self,theid,area_name,number,department,group_name,remarks ): #添加班组
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Group/edit_group"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid
        data["area_name"]=area_name
        data["number"]=number
        data["department"]=department
        data["group_name"]=group_name
        data["remarks"]=remarks

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {
				theid:'' //班组唯一码
			}
	'''
    def delete_group(self,theid): #删除班组
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Group/delete_group"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
				theid:'25241885',
				area_name: 'yeguoxiong', //区域名称
				number:'2',//部门编号
				pattern_card:'',/*模式卡号*/
				card_no:'',/*人员卡号*/
				dwcard_no:'', /*备用卡号*/
				enabled:'',/*是否可用*/
				group_number:'', /*班组编号，用于关联*/
				names:'',/*人员姓名*/
				age:'',/*年龄*/
				gender:'',/*姓别*/
				id_number:'',/*身份证号*/
				nation:'',/*民族*/
				birthday:'',/*生日*/
				id_organ:'',/*发证机关*/
				phone:'',/*电话*/
				unit:'',/*单位*/
				address:'',/*地址*/
				id_image:'',/*身份证图片*/
				remarks:''/*备注*/
			}
	'''
    def add_consumer(self,theid,area_name,number,pattern_card,card_no,dwcard_no,enabled,group_number,names,age,gender,id_number,nation,birthday,id_organ,phone,unit,address,id_image,remarks): #添加人员信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Consumer/add_consumer"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid
        data["area_name"]=area_name
        data["number"]=number
        data["pattern_card"]=pattern_card
        data["card_no"]=card_no
        data["dwcard_no"]=dwcard_no
        data["enabled"]=enabled
        data["group_number"]=group_number
        data["names"]=names
        data["age"]=age
        data["gender"]=gender
        data["id_number"]=id_number
        data["nation"]=nation
        data["birthday"]=birthday
        data["id_organ"]=id_organ
        data["phone"]=phone
        data["unit"]=unit
        data["address"]=address
        data["id_image"]=id_image
        data["remarks"]=remarks

        result=Proxy.send(self.url,data)
        return result #异常返回值为''


    '''
    {	
				theid:'',//用户信息唯一码
				area_name: 'yeguoxiong', //区域名称
				number:'2',//部门编号
				pattern_card:'',/*模式卡号*/
				card_no:'',/*人员卡号*/
				dwcard_no:'', /*备用卡号*/
				enabled:'',/*是否可用*/
				group_number:'', /*班组编号，用于关联*/
				names:'',/*人员姓名*/
				age:'',/*年龄*/
				gender:'',/*姓别*/
				id_number:'',/*身份证号*/
				nation:'',/*民族*/
				birthday:'',/*生日*/
				id_organ:'',/*发证机关*/
				phone:'',/*电话*/
				unit:'',/*单位*/
				address:'',/*地址*/
				id_image:'',/*身份证图片*/
				remarks:''/*备注*/
			}
	'''
    def edit_consumer(self,theid,area_name,number,pattern_card,card_no,dwcard_no,enabled,group_number,names,age,gender,id_number,nation,birthday,id_organ,phone,unit,address,id_image,remarks): #修改人员信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Consumer/edit_consumer"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid
        data["area_name"]=area_name
        data["number"]=number
        data["pattern_card"]=pattern_card
        data["card_no"]=card_no
        data["dwcard_no"]=dwcard_no
        data["enabled"]=enabled
        data["group_number"]=group_number
        data["names"]=names
        data["age"]=age
        data["gender"]=gender
        data["id_number"]=id_number
        data["nation"]=nation
        data["birthday"]=birthday
        data["id_organ"]=id_organ
        data["phone"]=phone
        data["unit"]=unit
        data["address"]=address
        data["id_image"]=id_image
        data["remarks"]=remarks

        result=Proxy.send(self.url,data)
        return result #异常返回值为''


    '''
    {	
				theid:'',//用户信息唯一码
			}
	'''
    def del_consumer(self,theid): #删除人员信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Consumer/del_consumer"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid

        result=Proxy.send(self.url,data)
        return result #异常返回值为''


    '''
    {	
					theid:'25241885',
					area_name:'yeguoxiong',//
					project_name:'中建三局拉林项目部',//
					workarea_name:'1工区',//
					names:'米拉山横洞',//
					place:'西藏省拉萨市米林县阿吉布鲁村',//
					longitude:'2',//
					latitude:'1',//
					is_added:'2',//
					update_time:'1',//
					remarks:'王刚' //
			}
    '''
    def add_location(self,theid,area_name,project_name,workarea_name,names,place,longitude,latitude,is_added,update_time,remarks ): #添加项目信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Location/add_location"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码
        data["area_name"]=area_name #工区标识名称
        data["project_name"]=project_name #项目名称
        data["workarea_name"]=workarea_name #工区名称
        data["names"]=names #隧道名称
        data["place"]=place #安装地址
        data["longitude"]=longitude #经度
        data["latitude"]=latitude #纬度
        data["is_added"]=is_added
        data["update_time"]=update_time #更新时间
        data["remarks"]=remarks #备注

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
					theid:'25241885',
					area_name:'yeguoxiong',//
					project_name:'中建三局拉林项目部',//
					workarea_name:'1工区',//
					names:'米拉山横洞',//
					place:'西藏省拉萨市米林县阿吉布鲁村',//
					longitude:'2',//
					latitude:'1',//
					is_added:'2',//
					update_time:'1',//
					remarks:'王刚' //
			}
    '''
    def edit_location(self,theid,area_name,project_name,workarea_name,names,place,longitude,latitude,is_added,update_time,remarks ): #修改项目信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Location/edit_location"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码
        data["area_name"]=area_name #工区标识名称
        data["project_name"]=project_name #项目名称
        data["workarea_name"]=workarea_name #工区名称
        data["names"]=names #隧道名称
        data["place"]=place #安装地址
        data["longitude"]=longitude #经度
        data["latitude"]=latitude #纬度
        data["is_added"]=is_added
        data["update_time"]=update_time #更新时间
        data["remarks"]=remarks #备注

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
					theid:'25241885',
			}
    '''
    def del_location(self,theid): #删除项目信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Location/del_location"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
				theid:'25241885',
				area_name:'yeguoxiong',//
				names:'叶国雄',//
				device_sn:'61111043',//
				pattern_card:'dw164256',//
				card_no:'123',//
				group_number:'2',//
				door_no:'1',//
				inOuts:'1',//
				swipe_status:'c1',//
				rssi_vale:'85',//
				update_time:'2018-01-05 13:02:01',//
				in_swipeimage:'',
				out_swipeimage:'',
				nX:'',
				nY:''
			}
    '''
    def add_mjswipe(self,theid,area_name,names,device_sn,pattern_card,card_no,group_number,door_no,inOuts,swipe_status,rssi_vale,update_time,in_swipeimage,out_swipeimage,nX,nY ): #添加刷卡状态信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Mjswipe/add_mjswipe"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码
        data["area_name"]=area_name #
        data["names"]=names
        data["device_sn"]=device_sn
        data["pattern_card"]=pattern_card
        data["card_no"]=card_no
        data["group_number"]=group_number
        data["door_no"]=door_no
        data["inOuts"]=inOuts
        data["swipe_status"]=swipe_status
        data["rssi_vale"]=rssi_vale
        data["update_time"]=update_time
        data["in_swipeimage"]=in_swipeimage
        data["out_swipeimage"]=out_swipeimage
        data["nX"]=nX
        data["nY"]=nY

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
				theid:'25241885',
			}
    '''
    def del_mjswipe(self,theid ): #删除刷卡状态信息接口
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Mjswipe/del_mjswipe"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
					theid:'25241885',
					area_name:'yeguoxiong',//
					pattern_card:'dw164256',//
					card_no:'123',//
					device_sn:'61111043',//
					door_no:'1',//
					reader_no:'2',//
					inOuts:'1',//
					swipe_status:'c1',//
					rssi_vale:'85',//
					nX:'',//
					nY:'',//
					swipe_image:'',//
					update_time:'2018-01-05 13:02:01'
			}
    '''
    def add_swipe_record(self,theid,area_name,pattern_card,card_no,device_sn,door_no,reader_no,inOuts,swipe_status,rssi_vale,nX,nY,swipe_image,update_time ): #添加刷卡状态信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Mjrecord/add_swipe_record"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码
        data["area_name"]=area_name #
        data["pattern_card"]=pattern_card
        data["card_no"]=card_no
        data["device_sn"]=device_sn
        data["door_no"]=door_no
        data["reader_no"]=reader_no
        data["inOuts"]=inOuts
        data["swipe_status"]=swipe_status
        data["rssi_vale"]=rssi_vale
        data["nX"]=nX
        data["nY"]=nY
        data["swipe_image"]=swipe_image
        data["update_time"]=update_time

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
					theid:'25241885',
			}
    '''
    def del_swipe_record(self,theid): #删除刷卡记录信息接口
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Mjrecord/del_swipe_record"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码

        result=Proxy.send(self.url,data)
        return result #异常返回值为''


    '''
    {	
					theid:'25241885',
					area_name:'yeguoxiong',//
					pattern_card:'dw164256',//
					card_no:'123',//
					in_datetime:'61111043',//
					out_datetime:'1',//
					working_msecs:'2',//
					update_time:'1'//
			}
    '''
    def add_attend(self,theid,area_name,pattern_card,card_no,in_datetime,out_datetime,working_msecs,update_time ): #添加考勤记录信息接口
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Attend/add_attend"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码
        data["area_name"]=area_name #
        data["pattern_card"]=pattern_card
        data["card_no"]=card_no
        data["in_datetime"]=in_datetime
        data["out_datetime"]=out_datetime
        data["working_msecs"]=working_msecs
        data["update_time"]=update_time
        result=Proxy.send(self.url,data)
        return result #异常返回值为''

    '''
    {	
					theid:'25241885',
			}
    '''
    def del_attend(self,theid): #删除考勤记录信息接口
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["cmd"]=self.doorUrl+self.subUrl+"/Attend/del_attend"
        data["user_name"]=self.username
        data["password"]=self.passwordMD5

        data["theid"]=theid #行唯一标识码

        result=Proxy.send(self.url,data)
        return result #异常返回值为''

if __name__ == '__main__':

    obj=Client("http://192.168.0.158",'Admin',"123")

    result=obj.get_heart('23')
    print(result)
    result=obj.add_location('1','实验区','项目','sdf','2','3','3.3','4.4','2019-01-01','')
    print(result)

