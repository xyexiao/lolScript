import os
import time
import random
from datetime import datetime
from enum import Enum

import win32api
import win32con
import win32gui
from PIL import ImageGrab
from PIL import Image

from c_keyboard import PressKey
from c_keyboard import ReleaseKey
from c_keyboard import PressLeftMouse
from c_keyboard import ReleaseLeftMouse
from c_keyboard import PressRightMouse
from c_keyboard import ReleaseRightMouse


CLIENT_TEXT = "League of Legends"
GAME_TEXT = "League of Legends (TM) Client"
SCREEN_SHOT_IMAGE = "screen_shot.png"
CLIENT_SIZE = (1280, 720)
RESIZE = (8, 8)
OUT_TIME = 180
SIMILAR_THRESHOLD = 0.9
LOG_FILE = "log.txt"
SAVE_IMAGE_DIR = os.path.join("tools", "images")
LOG = Enum("LOG", ("INFO", "WARN", "ERROR"))
KEY_CODE = {"Q": 16, "W": 17, "E": 18, "R": 19,
            "T": 20, "A": 30, "P": 25, "CTRL": 29}
SCAN_IMAGES = [{
    "funtion_name": "m_main_interface",
    "image": "images/1604840390.png",
    "scan": [(70, 20, 190, 60)]}, {
    "funtion_name": "m_select_play_way",
    "image": "images/1604840432.png",
    "scan": [(70, 0, 280, 70), (470, 670, 630, 700)]}, {
    "funtion_name": "m_create_game",
    "image": "images/1604840522.png",
    "scan": [(470, 670, 630, 700), (1130, 50, 1190, 70)]}, {
    "funtion_name": "m_in_line",
    "image": "images/1604840561.png",
    "scan": [(470, 670, 630, 700), (1130, 50, 1190, 70),
             (440, 410, 610, 500)]}, {
    "funtion_name": "m_find_game",
    "image": "images/1604840564.png",
    "scan": [(660, 370, 715, 405)]}, {
    "funtion_name": "m_accept_game",
    "image": "images/1604840624.png",
    "scan": [(660, 370, 715, 405)]}, {
    "funtion_name": "m_select_legend",
    "image": "images/1605108230.png",
    "scan": [(650, 10, 710, 40)]}, {
    "funtion_name": "m_select_ok",
    "image": "images/1605358654.png",
    "scan": [(431, 676, 444, 688), (825, 666, 857, 698)]}, {
    "funtion_name": "m_loading_game",
    "image": "images/1605108355.png",
    "scan": [(10, 500, 120, 700)]}, {
    "funtion_name": "m_game_live",
    "image": "images/1605358833.png",
    "scan": [(855, 680, 875, 700)]}, {
    "funtion_name": "m_game_deal",
    "image": "images/1604841291.png",
    "scan": [(855, 680, 875, 700)]}, {
    "funtion_name": "m_thanks",
    "image": "images/1604842188.png",
    "scan": [(625, 635, 655, 665)]}, {
    "funtion_name": "m_can_play_again",
    "image": "images/1605359817.png",
    "scan": [(430, 530, 700, 700)]}, {
    # "funtion_name": "m_not_play_again",
    # "image": "images/1604842566.png",
    # "scan": [(460, 600, 630, 700)]}, {
    "funtion_name": "m_connect_again",
    "image": "images/1606739565.png",
    "scan": [(475, 345, 570, 375)]}, {
    "funtion_name": "m_task_ok",
    "image": "images/1604842205.png",
    "scan": [(580, 660, 700, 690)]
}]


def log(message, level=LOG.INFO):
    """日志记录"""
    # with open(LOG_FILE, "a", encoding="utf8") as file_obj:
    #     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     file_obj.write(f"{now} <{level.name}> {message}\n")
    return


def window_click(handle, x, y, only_move=False, left=True):
    """
    左键单击窗口中位置(x, y)的点
    :param handle:窗口句柄
    :param x:横向坐标
    :param y:纵向坐标
    """
    try:
        window_position = win32gui.GetWindowRect(handle)
    except Exception as e:
        log(str(e), LOG.ERROR)
    win32api.SetCursorPos((window_position[0] + x, window_position[1] + y))
    if not only_move:
        if left:
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP,
                0, 0, 0, 0)
        else:
            win32api.mouse_event(
                win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP,
                0, 0, 0, 0)


def press_keyboard(key_code, ctrl=False):
    """按压键盘，支持CTRL组合键"""
    if ctrl:
        PressKey(KEY_CODE["CTRL"])
        time.sleep(0.1)
    PressKey(key_code)
    time.sleep(0.1)
    ReleaseKey(key_code)
    if ctrl:
        time.sleep(0.1)
        ReleaseKey(KEY_CODE["CTRL"])


def m_main_interface(handle):
    """主界面"""
    window_click(handle, 120, 40)
    time.sleep(1)
    return time.time()


def m_select_play_way(handle):
    """选择游戏类型"""
    window_click(handle, 160, 100)
    time.sleep(1)
    window_click(handle, 444, 533)
    time.sleep(1)
    window_click(handle, 540, 690)
    time.sleep(1)
    return time.time()


def m_create_game(handle):
    """创建游戏"""
    window_click(handle, 540, 690)
    time.sleep(1)
    return time.time()


def m_in_line(handle):
    """排队等待中"""
    time.sleep(1)
    return time.time()


def m_find_game(handle):
    """匹配到队伍"""
    window_click(handle, 640, 560)
    time.sleep(1)
    return time.time()


def m_accept_game(handle):
    """已同意游戏对局"""
    time.sleep(1)
    return time.time()


def m_select_legend(handle):
    """选择英雄"""
    # points = [(480, 100), (890, 160), (890, 350),
    #           (690, 355), (790, 260), (485, 160)]
    points = [(890, 160), (890, 350),
              (690, 355), (790, 260), (485, 160)]
    for point in points:
        window_click(handle, *point)
        time.sleep(1)
    window_click(handle, 640, 610)
    time.sleep(1)
    return time.time()


def m_select_ok(handle):
    """选择好了英雄"""
    return time.time()


def m_loading_game(handle):
    """游戏加载中"""
    time.sleep(5)
    return time.time()


def m_game_deal(handle):
    """在游戏中死亡"""
    press_keyboard(KEY_CODE["P"])
    time.sleep(0.5)
    for _ in range(2):
        window_click(handle, 555, 130, only_move=True)
        time.sleep(0.5)
        PressLeftMouse()
        time.sleep(0.5)
        ReleaseLeftMouse()
        time.sleep(0.5)
    for _ in range(2):
        window_click(handle, 375, 195, only_move=True)
        time.sleep(0.5)
        PressLeftMouse()
        time.sleep(0.5)
        ReleaseLeftMouse()
    for _ in range(2):
        window_click(handle, 665, 540, only_move=True)
        time.sleep(0.5)
        PressRightMouse()
        time.sleep(0.5)
        ReleaseRightMouse()
    press_keyboard(KEY_CODE["P"])
    return time.time()


def m_game_live(handle):
    """在游戏中存活"""
    # 点赞
    if random.randint(0, 9) > 6:
        press_keyboard(KEY_CODE["T"])
        press_keyboard(KEY_CODE["T"])
    # 升级技能
    press_keyboard(KEY_CODE["R"], ctrl=True)
    time.sleep(0.1)
    press_keyboard(KEY_CODE["Q"], ctrl=True)
    time.sleep(0.1)
    # 释放技能
    press_keyboard(KEY_CODE["Q"])
    time.sleep(0.1)
    # press_keyboard(KEY_CODE["R"])
    # time.sleep(0.1)
    # 进攻
    window_click(handle, 1340, 565, only_move=True)
    time.sleep(0.1)
    press_keyboard(KEY_CODE["A"])
    return time.time()


def m_thanks(handle):
    """点赞队友的界面"""
    window_click(handle, 640, 650)
    time.sleep(1)
    return time.time()


def m_can_play_again(handle):
    """再玩一次"""
    window_click(handle, 540, 680)
    time.sleep(1)
    return time.time()


def m_not_play_again(handle):
    """无法再玩一次"""
    window_click(handle, 445, 685)
    time.sleep(1)
    return time.time()


def m_task_ok(handle):
    """任务完成"""
    window_click(handle, 640, 680)
    time.sleep(1)
    return time.time()


def m_connect_again(handle):
    """重新连接"""
    window_click(handle, 520, 360)
    return time.time()


def get_size(rect):
    """通过两点坐标获取矩形的宽和高"""
    return (rect[2] - rect[0], rect[3] - rect[1])


def close_game():
    os.system('taskkill /F /IM "League of Legends.exe"')
    time.sleep(60)
    for i in range(10):
        win32api.SetCursorPos((180, 755))
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP,
            0, 0, 0, 0)
        time.sleep(2)


def close_client():
    os.system("taskkill /F /IM LeagueClientUx.exe")


def avg_Hash(image_data):
    """均值哈希算法"""
    data = image_data.resize(RESIZE, Image.ANTIALIAS).convert("L").getdata()
    avg = sum(data) / (RESIZE[0] * RESIZE[1])
    return [0 if i < avg else 1 for i in data]


def compare_images(image1, image2):
    """
    比较两种图片相似度
    :param image1:图片1的数据
    :param image2:图片2的数据
    :return: 百分比的相似度
    """
    ahash1 = avg_Hash(image1)
    ahash2 = avg_Hash(image2)
    same_bit = sum([1 if ahash1[i] == ahash2[i] else 0
                    for i in range(RESIZE[0] * RESIZE[1])])
    return same_bit / (RESIZE[0] * RESIZE[1])


def scan_model(now_image=SCREEN_SHOT_IMAGE):
    """
    通过图片判断当前阶段
    :param now_image: 截图
    :return: 阶段的方法名
    """
    max_model_value = 0
    now_data = Image.open(now_image)
    for image in SCAN_IMAGES:
        model_data = Image.open(image["image"])
        # 如果截图与模式的图片尺寸不相同，跳过
        if now_data.size != model_data.size:
            continue
        # 判断截图与当前模式的相似度
        value = 0
        for area in image["scan"]:
            value += compare_images(now_data.crop(area), model_data.crop(area))
        value = value / len(image["scan"])
        if value > max_model_value:
            max_model_value = value
            return_model = image["funtion_name"]
    if max_model_value < SIMILAR_THRESHOLD:
        return_model = None
        log("截图信息无法判断当前阶段", LOG.WARN)
    else:
        log(f"当前模式为:{return_model[2:]},置信度:{max_model_value}")
    return return_model


def get_client_handle():
    """获取游戏客户端的句柄"""
    handle = win32gui.FindWindow(None, CLIENT_TEXT)
    if handle:
        client_size = win32gui.GetWindowRect(handle)
        if get_size(client_size) != CLIENT_SIZE:
            child_handles = []
            win32gui.EnumChildWindows(
                handle, lambda h, l: l.append(h), child_handles)
            for child_handle in child_handles:
                child_size = win32gui.GetWindowRect(child_handle)
                if get_size(child_size) == CLIENT_SIZE:
                    handle = child_handle
                    break
    return handle


def get_screen_shot(image_save_dir=SCREEN_SHOT_IMAGE):
    """
    获取截图
    :return: 窗口句柄
    """
    game_handle = win32gui.FindWindow(None, GAME_TEXT)
    client_hanle = get_client_handle()
    handle = game_handle if game_handle else client_hanle
    if not handle:
        log("客户端和游戏程序都不存在", LOG.WARN)
    else:
        try:
            window_position = win32gui.GetWindowRect(handle)
            win32gui.SetForegroundWindow(handle)
            time.sleep(1)
            ImageGrab.grab(window_position).save(image_save_dir)
        except Exception as e:
            log(str(e), LOG.ERROR)
            handle = 0
    return handle


if __name__ == "__main__":
    last_action_time = time.time()
    while True:
        handle = get_screen_shot()
        if handle:
            last_action_time = locals().get(
                scan_model(), lambda x: last_action_time)(handle)
        if (time.time() - last_action_time) > OUT_TIME:
            if handle:
                # 保持截图并写入LOG
                get_screen_shot(os.path.join(
                    SAVE_IMAGE_DIR, str(int(time.time())) + ".png"))
                log("长时间无法识别图片信息来判断当前阶段，程序退出", LOG.ERROR)
                break
            else:
                close_game()
                last_action_time = time.time()
                log("长时间未检测到客户端和游戏程序，重启游戏", LOG.ERROR)
        time.sleep(1)
