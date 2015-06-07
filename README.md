beefapi
=======

Python library that facilitates interacting with [BeEF](http://beefproject.com/) via it's RESTful API

Requires Python 2.7 and the ```requests``` library

Examples
========

- import the library and login to BeEF
```
In [1]: from core.beefapi import BeefAPI

In [2]: beef = BeefAPI({})

In [3]: beef.login('beef', 'beef')
Out[3]: True

```
- Print the id and name of all available modules:
```
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
```
In [7]: for module in beef.modules.findbyname('d-link'):
   ...:     print module.id, module.name
   ...:     
88 D-Link DSL-2740R DNS Hijack
67 D-Link DIR-615 Password Wipe
120 D-Link ShareCenter Command Execution
81 D-Link DSL-2640B DNS Hijack
80 D-Link DSL500T CSRF

```

- Print the id, browser and os of all online hooked browsers
```
In [13]: for hook in beef.hooked_browsers.online:
    print hook.id, hook.name, hook.os
   ....:     
2 FF Windows 8.1
```

- Run a module against all online hooked browsers:
```
In [14]: for hook in beef.hooked_browsers.online:
   ....:     print hook.run(223)
   ....:     
{u'success': u'true', u'command_id': u'4'}
```

- Get the results of the previously executed module
```
In [18]: session = beef.hooked_browsers.online[0].session

In [20]: beef.modules.findbyid(223).results(session, 4)
Out[20]: 
{u'0': {u'data': u'{"data":"result=Rickroll Successful"}',
  u'date': u'1433706868'}}
```

