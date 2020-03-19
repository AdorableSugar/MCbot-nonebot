# -*- coding:utf-8 -*-
from nonebot import on_command, CommandSession
import requests
from xml.etree import ElementTree

@on_command('bug')

async def bug(session: CommandSession):
    try:
        stripped_arg = session.current_arg_text.strip()
        session.state['pagename'] = stripped_arg
        pagename = session.get('pagename')
        url_str ='https://bugs.mojang.com/si/jira.issueviews:issue-xml/'+ pagename + '/' + pagename + '.xml'
        respose_str =  requests.get(url_str)
        respose_str.encoding = 'utf-8'
        root = ElementTree.XML(respose_str.text)
        try:
            for node in root.iter("channel"):
                for node in root.iter("item"):
                    Title = node.find("title").text
                    Type = "Type:" + node.find("type").text
                    Project = "Project:" + node.find("project").text
                    TStatus = "Status:" + node.find("status").text
                    Resolution = "Resolution:" + node.find("resolution").text
                    Version = "Version:" + node.find("version").text
                    Link = node.find("link").text
                    await session.send(Title+'\n'+Type+'\n'+Project+'\n'+TStatus+'\n'+Resolution+'\n'+Version+'\n'+Link)
        except Exception:
            await session.send("发生错误：此漏洞不存在。")
    except Exception:
        await session.send("发生错误：土豆熟了。")