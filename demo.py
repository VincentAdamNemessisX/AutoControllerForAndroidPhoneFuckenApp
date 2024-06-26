# Author: 
# created_time:
import os
import random
import time

from pypinyin import lazy_pinyin


def execute(cmd):
    adb_path = '/Users/vincent/TempFolder/MaybeUsefulWithShortTime/platform-tools/'
    adb_str = adb_path + 'adb shell {}'.format(cmd)
    # print(adb_str)
    os.system(adb_str)


times = 1


def get_next_photo():
    # 检查是否提供了初始位置
    positions = [
        (330, 535), (772, 535),
        (330, 1200), (772, 1200),
        (330, 1850), (772, 1850)
    ]
    return positions[random.randint(0, len(positions) - 1)]


def select_type_logic(tpe='室内卫生'):
    enum = {
        '室内卫生': '',
        '室外卫生': 'input swipe 598 2018 598 1892',
        '宿舍值日': 'input swipe 598 2002 598 1850',
        '家庭劳动': 'input swipe 598 2018 598 1770',
        '临时性劳动': 'input swipe 598 2018 598 1589'
    }
    execute('input tap 860 281')
    time.sleep(0.5)
    if tpe != '室内卫生':
        execute(enum[tpe])
        time.sleep(0.5)
    execute('input tap 974 1570')
    time.sleep(0.5)


def select_time_logic(start=True, start_time=None):
    if start:
        execute('input tap 860 417')
        time.sleep(0.5)
        year_y_value = [1100, 1200]  # 2024 2023 2022
        year_y_index = random.randint(0, len(year_y_value) - 1)
        execute('input swipe 140 2000 140 ' + str(year_y_value[year_y_index]))
        time.sleep(0.2)
        month_y_value = [2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200,
                         1100, 1000, 900]
        month_y_index = random.randint(0, len(month_y_value) - 1)
        execute('input swipe 370 2000 370 ' + str(month_y_value[month_y_index]))
        time.sleep(0.2)
        day_y_value = [2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100,
                       1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0,
                       -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]  # 30-1
        day_y_index = random.randint(0, len(day_y_value) - 1)
        execute('input swipe 557 2000 557 ' + str(day_y_value[day_y_index]))
        time.sleep(0.2)
        hour_y_value = [2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100,
                        1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]
        hour_y_index = random.randint(0, len(hour_y_value) - 1)
        execute('input swipe 760 2000 760 {}'.format(str(hour_y_value[hour_y_index])))
        time.sleep(0.2)
        execute('input tap 1005 1637')
        time.sleep(0.5)
        return [year_y_value[year_y_index], month_y_value[month_y_index],
                day_y_value[day_y_index], hour_y_value[hour_y_index]]
    else:
        execute('input tap 840 532')
        time.sleep(0.5)
        execute('input swipe 140 2000 140 {}'.format(str(start_time[0])))
        time.sleep(0.2)
        execute('input swipe 370 2000 370 500')
        execute('input swipe 370 2000 370 500')
        execute('input swipe 370 2000 370 500')
        time.sleep(0.1)
        execute('input swipe 557 2000 557 {}'.format(str(start_time[2] - 100)))
        time.sleep(0.2)
        execute('input swipe 760 2000 760 {}'.format(str(start_time[3] - 100)))
        time.sleep(0.2)
        execute('input tap 1005 1637')
        time.sleep(0.5)
        return None


def fill_event_text(event):
    execute('input tap 890 651')
    time.sleep(0.5)
    execute('input tap 350 430')
    time.sleep(0.2)
    execute('input text {}'.format(str(event)))
    time.sleep(0.5)
    execute('input text {}'.format(str(1)))
    time.sleep(0.5)
    execute('input tap 570 870')
    time.sleep(0.2)


def select_and_upload_photo_logic(pos=(330, 1130)):
    global times
    execute('input tap 885 823')  # 点击‘上传图片’
    time.sleep(0.5)  # 等待弹出
    execute('input tap 200 1790')  # 点击‘选择照片’
    time.sleep(0.3)
    execute('input tap 1006 405')  # 点击‘...’
    time.sleep(0.5)
    execute('input tap 700 420')  # 点击‘browse’
    time.sleep(0.7)
    execute('input tap 85 143')
    time.sleep(0.5)
    execute('input tap 310 498')
    time.sleep(0.5)
    execute('input tap 308 1124')  # 点击‘Camera文件夹’
    time.sleep(0.3)
    execute('input swipe 545 1150 545 642')  # 滑动到初始位置
    time.sleep(0.3)
    for _ in range((times - 1) // 6):
        execute('input swipe 545 1947 545 647')
        time.sleep(0.3)
    times += 1
    execute('input tap {} {}'
            .format(pos[0], pos[1]))  # 选择图片
    time.sleep(2.8)


def cycle_logic(tpe='室内卫生'):
    execute('input tap 528 2273.6')  # 点击‘新增登记’
    time.sleep(1.5)
    # 选择登记类型逻辑
    select_type_logic(tpe)
    # 选择劳动开始时间
    start_time = select_time_logic()
    # 选择劳动结束时间
    select_time_logic(start=False, start_time=start_time)
    # 输入劳动事务
    event = ''.join(lazy_pinyin(tpe))
    fill_event_text(event)
    # 上传图片逻辑
    select_and_upload_photo_logic(get_next_photo())
    # select_and_upload_photo_logic(get_next_photo())
    execute('input tap {} {}'.format('545', '2288'))
    time.sleep(2)


if __name__ == '__main__':
    for i in range(2):
        times = 1
        for j in range(12):
            cycle_logic('宿舍值日')
            print('第{}次提交完成'.format(str((times - 1))))
        print('第{}轮已完成，\n第{}轮开始'.format(str(i + 1), str(i + 2)))
