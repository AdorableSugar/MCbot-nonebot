# -*- coding:utf-8 -*-
from nonebot import on_command, CommandSession
import requests
import json
import time

@on_command('mcv-loop')

async def mcvloop(session: CommandSession):
    url = 'http://launchermeta.mojang.com/mc/game/version_manifest.json'
    try:
        version_manifest = requests.get(url)
        file = json.loads(version_manifest.text)
        await session.send("最新版：" + file['latest']['release'] + "，最新快照：" + file['latest']['snapshot']+"，已开始20秒检测一次，侦测到新版本后将发送消息。")
        while True:
            if file['latest']['snapshot']=="20w11a":
                await session.send("呐，最新版：" + file['latest']['release'] + "，最新快照：" + file['latest']['snapshot']+"惹。")
                break
            else:
                print("没有侦测到新版本。")
            time.sleep(20)
    except Exception:
        try:
            time.sleep(20)
        except Exception:
            await session.send("发生错误：土豆熟了。")

