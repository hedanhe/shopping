from shopping.common import *
import json
from flask import render_template
import socket

app.secret_key = b'D\xb2\x9b\xea(9\'\xa0\xaci\xa1"\x87\xe5\x97h^v\xa1\
                x9cY {G!\xa7P$\xacW\xc7\xe6\xb5\xea[\x04\x18\x13\'\xe2\
                x89\xd3X\xf3u\x9e\xe4\xf7-z;O\x84T\xea\xdcl\xf4Wf7r\xacC\
                x1e\xc6}\xe2\xdf\x8b\x10\xbc\x1d\x8e\xc7\x15\xcd\x82\x86\
                xca\xeba\xcc\xe6\x90\xe5?TV\x9deZ\xbdwVW\xf18P#\xcaO\xcd\
                x19\xaf\xb9\x98\xceM\x12M\xc0\x8ep\xfc\xac_,\n\xe4\xc1\
                x0fmJ5\x9f\xf8Jt\x8b@\xafN\x87VA\xfa\x1a\xdc\x9dS\x8e\
                xac}\x9e\n\xbf^\xd0\x0e8\xa9M\x05\xf9=\xfa2\xd5\x02\xc5\
                x04\xa4\x18\x10\x82\xedg\xd3\xa8\xd3h\xba\x05\xba\x14neQ\
                xa5\xa1\x13u\xc2:\x04\xa8\xe8\xb7\xef\x88NNdpd\xbbU\xc1\xe5\
                x10\xea\xf1i\xa5\xf39q-\xd0hFt\x85v\xca\x9e\x7fw\xb3}\x93W1^\
                x8c\xaf\xfat\x1d\xfe\xa5g\x83\x88\xea\xebT/\xd9\x9f*h\xbb:\
                xe1C\xceL\x86\x11l\x9e\x1f\xfd\x91hX\x97e\x86\xa9\xe5\xb3\x07\
                xd0\x8cH\xc6}\xcd6\xa1B\x8a\x0e\xd6\x1cD`\xb6b\xa45k\x1elI\xd7\
                xe7\xf8\xcc\x1c\xa3\xe9"w?Z\xec?s\xa7v\x81\xa8\x19\xc1\xa8a&\x86s\
                xf9\xa76^\xf6\x13\x02\x7f(\xa8\xd6\xfc\x02\xe7p\xca\x16\xfc\t\x15\
                xa4-q\xbb\x18\x04\x02C)\xb4B\x07\xd0W|m\xc9\xc0\x0e:\x18w\xd5\xb4\
                x98NY\xd66.\xca\xf0c\xd35y\xfa\xef\xd2\xa8\xc1\x03O\xf8.\xa4$\x14f\
                x10>\x9a\xd2\xa39z\xbe\x9d\t:\xcf,\xcfL9#lZ\xe5\x85\xe0\x1f\xb4UQ6=+\
                xe8\x96pJE\xae\xa4\xee\x88\x13\x18\x06\xb4O*\xfb\x87\xd8I\xa65\xf5\xfa\
                x0b\xcf\xc4\x97\xfc5\x8d\xe3:\x05\xdc\x97\x12XvP\xbe\x11\x91\x87+b\
                x04\xf9\xaf\x12G\xb1\x1e^H\x1b`\x8c\xd8B\xealk(\xfd!\x81\xebVSf\xc1\
                x05\xcb\xe5Rr\x9c5\x03~3\xbaC\x98\xdf\xee&\xd3I\xff\xe7e\x8c0D\x8aQ1\
                x8a\xb0\x94\xb2"\x93S\xe9Rm\xb4\xca>\x13\xf2ti2\xbc\xf3\xcd\x15\xe8\
                xf5\xea\xf0\xe2\x98c\x8a\xb3\x11k+\x06\xe4\xf3\xa2\xdd@\x87I\xe2\x95\
                x93\x98\x0f\xde\\\xc8pg\n.\x0c\xe3 :\xdaur\x93\nz\xa4\xa6\x03\x95\x8eA\
                x11\xb3\xa5)\n\x8c,Y\x02\n6\xf0IV\xc2-\xad\xf5\xcf,F\xeb\xd0\xdeE\x1eK\
                xd2\xc4yxF2Qr\xf2\xd9\x91\x87:(5\xa2\x97h\x88\xcc\xc9\xd7b\xd8=>\xe8V\
                xffR\'\xbaV\x82\xc2MOd\x9a\x1e\xe9n\r\xea\x99\xcd\x8c\xa4j\x95Ww\r+\xb85C\
                t\xe4\x1d\xf1\xbc\xdf\x1d\xf1Y#\xe0m(4S\r\xd1\x7f\xdcR/\x8e\x91;\xd6\x14x\
                xf9}\x9d\x8fP\x8d"h;\\\x9b\xf1Bx\x15\xdbr\xa33\x9a>\xf5\xce7\xe3\xac4q\xddE\
                x8d<+%\xe2\xa1;\x08\x01n\xe8f\xec\'q\x87\xc5\x87\xd7\x84{\x04\xa0]\xb2\x94-C\
                x82\x88e\x85\xdd%!\xc8E\xd0\x90\x88\xdc\x17\\%\x86\x7f\x00\x19\xe6\xdb$\xef`\
                xfew\xaeQ1\xdau\xb7\xf8#\x97\xa1\x00\xfe\xa7N\xb4\xdf\x02\xff\x98X\xc0={R\
                x87gl#\xe5!\xd3hX\x18\xf9#\xed\x1c\x07u\xf1\x8e{\xdeB{A\xa0\xb2'

query = Query()
db = query.conn()

@app.route('/')
def first():
    navLi = getNavli()
    print(navLi)
    detailContent = getDetailContent()
    # print(detailContent)
    return render_template("index.html", navLi=navLi, detailContent=detailContent)

def getNavli():
    # 获取navli分类
    currsor = db.cursor()
    sql = "select * from nav_li where flag=1"
    try:
        currsor.execute(sql)
        results = currsor.fetchall()
        """要转为字典"""
        fields = ["cat_id", "index", "title"]
        arr = {}
        for i in range(len(results)):
            if results[i][1] in arr:
                arr[results[i][1]].append(results[i])
            else:
                arr[results[i][1]] = [results[i]]

        res_dict = []
        for j in range(len(arr)):
            mid_dict = []
            for item in arr[j+1]:
                nav_dict = dict(zip(fields,(item[0],str(item[1])+"_"+str(item[2]), item[3])))
                mid_dict.append(nav_dict)
            res_dict.append(mid_dict)

        return res_dict
    except:
        return None

def getDetailContent():
    #获取子分类
    currsor = db.cursor()
    sql = "select cat_id, a_index, b_index, title from detail_content where flag=1"
    try:
        currsor.execute(sql)
        results = currsor.fetchall()
        fields = ["cat_id", "index", "title"]
        arr = {}
        for i in range(len(results)):
            if results[i][1] in arr:
                if results[i][2] in arr[results[i][1]]:
                    arr[results[i][1]][results[i][2]].append(results[i])
                else:
                    arr[results[i][1]][results[i][2]] = [results[i]]

            else:
                arr[results[i][1]]={}
                arr[results[i][1]][results[i][2]] = [results[i]]

        res_dict = []
        for ja in range(1, len(arr)+1):
            mid_dict = []
            for jb in range(1,len(arr[ja])+1):
                nav_list = []
                for item in arr[ja][jb]:
                    nav_dict = dict(zip(fields, (item[0], str(item[1]) + "_" + str(item[2]), item[3])))
                    nav_list.append(nav_dict)
                mid_dict.append(nav_list)
            res_dict.append(mid_dict)
        return res_dict



    except Exception as e:
        print("11111111111")
        return e
    db.close()



if __name__ == '__main__':
    app.run()
