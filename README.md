BeEF-API
=======

Python library that facilitates interacting with [BeEF](http://beefproject.com/) via it's RESTful API

Requires Python 2.7 and the ```requests``` package (```pip install requests```)

Examples
========

- import the library and login to BeEF
```python
In [1]: from beefapi import BeefAPI

In [2]: beef = BeefAPI({})

In [3]: beef.login('beef', 'beef')
Out[3]: True

```
- Print the id and name of all available modules:
```python
In [10]: for module in beef.modules:  
   ....:     print module.id, module.name
   ....:
222 Replace HREFs (HTTPS)
223 Redirect Browser (Rickroll)
220 Replace Videos
221 Fingerprint Ajax
218 iOS Address Bar Spoofing
219 Redirect Browser
216 Get Cookie
217 Get Page HREFs

-- SNIP --     
```

- Find all modules containing the string 'd-link' and print their id and name:
```python
In [7]: for module in beef.modules.findbyname('d-link'):
   ...:     print module.id, module.name
   ...:     
88 D-Link DSL-2740R DNS Hijack
67 D-Link DIR-615 Password Wipe
120 D-Link ShareCenter Command Execution
81 D-Link DSL-2640B DNS Hijack
80 D-Link DSL500T CSRF

```

- Find all online hooked browsers that have the string 'windows' in their OS attribute
```python
In [7]: beef.hooked_browsers.online.findbyos('windows')
Out[7]: [<core.beefapi.Session object at 0x7f24b40dd710>]

In [8]: beef.hooked_browsers.online.findbyos('windows')[0].id
Out[8]: 2

In [9]: beef.hooked_browsers.online.findbyos('windows')[0].session
Out[9]: u'0EbkU7OUmaLBSGOtcdy43wMIh1r2VtU7O2QHsSzYJKONQCJ90gMnj53CQOQnZ9IfNIkr5SLBde1puw3v'

In [10]: beef.hooked_browsers.online.findbyos('windows')[0].name
Out[10]: u'FF'

In [11]: beef.hooked_browsers.online.findbyos('windows')[0].details
Out[11]: 
{u'BrowserLanguage': u'en-US',
 u'BrowserName': u'FF',
 u'BrowserPlatform': u'Win32',
 u'BrowserPlugins': u'Google Update-v.1.3.27.5,Java Deployment Toolkit 6.0.300.12-v.6.0.300.12,Silverlight Plug-In-v.5.1.40416.0',
 u'BrowserReportedName': u'Mozilla/5.0 (Windows NT 6.3; rv:38.0) Gecko/20100101 Firefox/38.0',
 u'BrowserType': u'{"C19iOS":null,"C20iOS":null,"C21iOS":null,"C22iOS":null,"C23iOS":null,"C24iOS":null,"C25iOS":null,"C26iOS":null,"C27iOS":null,"C28iOS":null,"C29iOS":null,"C30iOS":null,"C31iOS":null,"C32iOS":null,"C33iOS":null,"C34iOS":null,"C35iOS":null,"C36iOS":null,"C37iOS":null,"C38iOS":null,"C39iOS":null,"C40iOS":null,"C41iOS":null,"C42iOS":null,"C":null,"FF38":true,"FF":true}',
 u'BrowserVersion': u'38',
 u'CPU': u'32-bit',

 -- SNIP--
```

- Print the id, browser and os of all online hooked browsers
```python
In [13]: for hook in beef.hooked_browsers.online:
    print hook.id, hook.name, hook.os
   ....:     
2 FF Windows 8.1
```

- Run a module against all online hooked browsers:
```python
In [14]: for hook in beef.hooked_browsers.online:
   ....:     print hook.run(223)
   ....:     
{u'success': u'true', u'command_id': u'4'}
```

- Get the results of the previously executed module
```python
In [25]: beef.hooked_browsers.online
Out[25]: [<core.beefapi.Session object at 0x7f079cd89090>]

In [18]: session = beef.hooked_browsers.online[0].session

In [20]: beef.modules.findbyid(223).results(session, 4)
Out[20]: 
{u'0': {u'data': u'{"data":"result=Rickroll Successful"}',
  u'date': u'1433706868'}}
```

