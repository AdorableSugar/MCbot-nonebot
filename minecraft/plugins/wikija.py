import copy
import requests
import json
from nonebot import on_command, CommandSession

@on_command('wiki-ja')

async def wikija(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    session.state['pagename'] = stripped_arg
    pagename = session.get('pagename')
    metaurl = 'https://minecraft-ja.gamepedia.com/api.php?action=query&format=json&prop=info&inprop=url&titles='
    try:
        url = metaurl+pagename
        metatext = requests.get(url)
        file = json.loads(metatext.text)
        try:
            x = file['query']['pages']
            y = sorted(x.keys())[0]
            z = x[y]['fullurl']
            if  int(y) == -1:
                await session.send('找不到条目。')
            else:
                await session.send('您要的'+pagename+"："+z)
        except  Exception:
            await session.send('发生错误：内容非法。')
    except  Exception:
        await session.send('发生错误：土豆可能熟了。')