import re
import requests
import json
from nonebot import on_command, CommandSession

@on_command('server-raw')

async def serverraw(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    session.state['address'] = stripped_arg
    address = session.get('address')
    matchObj = re.match( r'(.*):(.*).*', address, re.M|re.I)
    try:
        if matchObj:
            url = 'http://motd.wd-api.com/?ip='+matchObj.group(1)+'&port='+matchObj.group(2)+'&mode=info'
            motd = requests.get(url)
            file = json.loads(motd.text)
            try:
                if file['code'] == 200:
                    x=re.sub(r'§\w',"",file['data']['description']['text'])
                    if not x:
                        extra = file['data']['description']['extra']
                        await session.send(str(extra)+"\n"+"在线玩家："+str(file['data']['players']['online'])+"/"+str(file['data']['players']['max'])+"\n"+"游戏版本："+file['data']['version']['name'])
                    else:
                        await session.send(x+"\n"+"在线玩家："+str(file['data']['players']['online'])+"/"+str(file['data']['players']['max'])+"\n"+"游戏版本："+file['data']['version']['name'])
                else:
                    await session.send("连接服务器失败。")
            except Exception:
                await session.send("发生错误：调用API时发生错误。")
        else:
            url = 'http://motd.wd-api.com/?ip='+address+'&port=25565&mode=info'
            motd = requests.get(url)
            file = json.loads(motd.text)
            try:
                if file['code'] == 200:
                    x=re.sub(r'§\w',"",file['data']['description']['text'])
                    if not x:
                        extra = file['data']['description']['extra']
                        await session.send(str(extra)+"\n"+"在线玩家："+str(file['data']['players']['online'])+"/"+str(file['data']['players']['max'])+"\n"+"游戏版本："+file['data']['version']['name'])
                    else:
                        await session.send(x+"\n"+"在线玩家："+str(file['data']['players']['online'])+"/"+str(file['data']['players']['max'])+"\n"+"游戏版本："+file['data']['version']['name'])
                else:
                    await session.send("连接服务器失败。")
            except Exception:
                await session.send("发生错误：调用API时发生错误。")
    except Exception:
        await session.send("发生错误：未知原因。")