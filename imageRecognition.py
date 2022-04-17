from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '23642440'
API_KEY = 'hbY0dSexZzqhgrwzehkbjnLT'
SECRET_KEY = 'oSX8LeRe4ZWIXryMEXc9Nzf8Yk7lUriA'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_img_rec(file,schema):
    image = get_file_content(file)

    if schema == "通用识别":
        """ 如果有可选参数 """
        options = {}
        options["baike_num"] = 5

        """ 带参数调用通用物体和场景识别 """
        result = client.advancedGeneral(image,options)["result"]
        keyword = result[1]["keyword"]
        baike_url = result[1]["baike_info"]["baike_url"]
        image_url = result[1]["baike_info"]["image_url"]
        description = result[1]["baike_info"]["description"]

        info = "图像主体类别: "+keyword +"\n"+"百度百科url: "+baike_url+"\n"+\
            "百度百科图片_url: "+image_url+"\n"+"描述: "+description
        return info
    elif schema == "动物识别":
        """ 如果有可选参数 """
        options = {}
        options["top_num"] = 3
        options["baike_num"] = 5

        """ 带参数调用动物识别 """
        result = client.animalDetect(image, options)["result"]
        keyword = result[1]["name"]
        score = result[1]["score"]
        info = "动物名称: " + keyword + "\n" + "置信度: "+score
        return info
    elif schema == "植物识别":
        """ 如果有可选参数 """
        options = {}
        options["baike_num"] = 5

        """ 带参数调用植物识别 """
        result = client.plantDetect(image, options)["result"]
        keyword = result[1]["name"]
        score = str(result[1]["score"])
        info = "植物名称: " + keyword + "置信度: " + score
        return info
    elif schema == "红酒识别":
        result = client.redwine(image)["result"]["wineNameCn"]
        return result
    elif schema == "货币识别":
        result = client.currency(image)["result"]
        cur_name = result["currencyName"]
        cur_domin = result["currencyDenomination"]

        info = "货币种类: "+cur_name+"\n"+"货币面值: "+cur_domin
        return info

# get_img_rec("images/cash.png","通用识别")
