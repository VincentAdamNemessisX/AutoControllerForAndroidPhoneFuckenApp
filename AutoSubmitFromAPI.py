# Author: VincentAdamNemessis
# created_time:
import random
import time

import requests
from loguru import logger


def init_type(tpe: str):
    labour_type = {
        "室内卫生": "01",
        "室外卫生": "02",
        "宿舍值日": "03",
        "家庭劳动": "04",
        "临时性劳动": "05",
    }
    try:
        return labour_type[tpe]
    except Exception as _:
        logger.warning("初始化劳动类型有误，已调整为默认值")
        return labour_type["室内卫生"]


def init_start_time_and_end_time(source: int, to: int):
    year = random.randint(source, to)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(6, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    start_time = (str(year) + "-" + str(month) + "-" + str(day)
                  + " " + str(hour) + ":" + str(minute) + ":" + str(second))
    end_time = (str(year) + "-" + str(month) + "-" + str(day)
                + " " + str(hour) + ":" + str(minute + 20) + ":" + str(second))
    return [start_time, end_time]


def init_content(content):
    return str(content)


def init_img_path(start: int, end: int, current: int):
    if end >= (current + 1) >= start:
        return "img/" + str(current + 1) + ".png"
    else:
        logger.warning("图片序号超出范围，已调整为默认值")
        return "img/" + str(start) + ".png"


def upload_img(x_id_token: str, file_path: str):
    headers = {
        "X-Id-Token": x_id_token
    }
    try:
        files = {
            "file": open(file_path, "rb")
        }
        response = requests.post(
            url="https://stuworkapp.sqgxy.edu.cn/api/blade-resource/oss/endpoint/put-file",
            headers=headers,
            files=files)
        files["file"].close()
        return response.json().get("data").get("link")
    except FileNotFoundError:
        logger.error("所选图片不存在")
        return ""
    except Exception as _:
        logger.error("上传图片失败")
        return ""


def init_stamp():
    stamp = int(time.time())
    return stamp


def init_end_point():
    return str('app')


def init_headers(x_id_token: str):
    headers = {
        "X-Id-Token": x_id_token,
        "Content-Type": "application/json"
    }
    return headers


def submit_data(x_id_token: str, labour_type: str, times: int, current: int):
    headers = init_headers(x_id_token)
    content = init_content(labour_type)
    labour_type = init_type(labour_type)
    img_path = init_img_path(1, times, current)
    tm = init_start_time_and_end_time(2022, 2024)
    start_time = tm[0]
    end_time = tm[1]
    stamp = init_stamp()
    try:
        response = requests.post(
            url="https://stuworkapp.sqgxy.edu.cn/api/supwisdom-stuwork-secendclass/v1/api/secondclass/labour/submit",
            headers=headers,
            json={
                "labourType": labour_type,
                "labourContent": content,
                "labourStartTime": start_time,
                "labourEndTime": end_time,
                "labourImg": upload_img(x_id_token, img_path),
                "stamp": stamp,
                "endPoint": init_end_point()
            })
        if response.status_code == 200:
            if response.json().get("code") != 200:
                logger.error("提交数据失败")
        else:
            logger.error("提交数据失败")
    except Exception as _:
        logger.error("提交数据失败")


def main():
    try:
        x_id_token = input("请输入X-Id-Token: ")
        while True:
            print()
            labour_type = input("请输入劳动类型(室内卫生/室外卫生/宿舍值日/家庭劳动/临时性劳动，退出输入退出): ")
            if labour_type == "退出":
                break
            times = int(input("请输入劳动次数: "))
            for i in range(times):
                submit_data(x_id_token, labour_type, times, i)
                logger.info("第{}次{}已完成\n".format(i + 1, labour_type))
    except Exception as _:
        logger.error("程序出错")


if __name__ == '__main__':
    main()
