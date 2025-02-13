# Documentation & Question

* [`Set up import all module`](#SetupModule)
* [`How to login?`](#loginFB)
* [`How to check Live/Die cookie?`](#checkCookie)
* [`How to receive message Thread?`](#receiveThread)
---------------------------------------

<a name="SetupModule"></a>
### Set up import all module

Please create a file and *install all the modules* present in here (main.py, mainBot.py, ...). **Example code:**
```python
import __facebookLoginV2
import __facebookToolsV2
import __messageListen
```
**NOTE**: Please create a file inside `fbchat-v2/src` :DD

<a name="loginFB"></a>
### How to login?

⚠️***WARNING***: **Facebook's Cookie & AccessToken** are very *crucial*. Malicious actors can peek at them on your screen when displayed, or even hackers attacking your computer (*botnet*) might steal them, and the risk to your Facebook account is very high! You can learn more about this [here](https://www.facebook.com/privacy/policies/cookies/?_rdr).

#### 1.Login with Account

**Notes:** You can access this library by logging in with your account/password and two-factor authentication code (if available) Facebook. However, we encourage users to use the Facebook Cookie instead of logging in with account/password.

*🦖*In the `src` of **fbchat-v2**, there is a file named *__facebookLoginV2.py*. Call it and fill in the arguments it requires (details below).

**__Arguments__**:

* `username`: Numberphone/gmail or ID user.
* `password`: Password for Account.
* `2fa`: Two-factor authentication code (if available)

Below is the sample code:

```python
user = "minhhuydev@icloud.com"
passw = "30102007"
twofa = None
clientLogin = __facebookLoginV2.loginFB(user, passw, twofa)
resultLogin = clientLogin.main()
print(resultLogin)
```

When running the above code, it will produce two outcomes (Success or Failure). Below is the `dict` when the login is **successful**:
```python
{'success': {'setCookies': 'c_user=61551671683861; xs=8:51DRVMpDOiHp1A:2:1698481000:-1:8465; fr=0KEtD6nFFrfDEKrJV.AWUAsJnjqK5VxFhFxfHxW8yzaeQ.BlPMNo..AAA.0.0.BlPMNo.AWUl1XTH5G8; datr=aMM8Zb2qBmtztvpdwwrykC6-; ', 'accessTokenFB': 'EAAAAUaZA8jlABO5DKmmquwPkzDdxUcwJ6CKPOqFh0gZBGl8HRhp1o9KhjRsVdXZCMA40JGPLuLxAYsDG6uIKJBPFGfl2iILzknxFfNidfLjICpikgDU2pFzQ4swhb0QUBtVACu3eGH61kBuRr0zQBytGbj9SzmnrK0mujr6wjSZBbCtfgdpwcRwPi8no6Dqb0gZDZD', 'cookiesKey-ValueList': [{'name': 'c_user', 'value': '61551671683861', 'expires': 'Sun, 27 Oct 2024 08:16:40 GMT', 'expires_timestamp': 1730017000, 'domain': '.facebook.com', 'path': '/', 'secure': True, 'samesite': 'None'}, {'name': 'xs', 'value': '8:51DRVMpDOiHp1A:2:1698481000:-1:8465', 'expires': 'Sun, 27 Oct 2024 08:16:40 GMT', 'expires_timestamp': 1730017000, 'domain': '.facebook.com', 'path': '/', 'secure': True, 'httponly': True, 'samesite': 'None'}, {'name': 'fr', 'value': '0KEtD6nFFrfDEKrJV.AWUAsJnjqK5VxFhFxfHxW8yzaeQ.BlPMNo..AAA.0.0.BlPMNo.AWUl1XTH5G8', 'expires': 'Fri, 26 Jan 2024 08:16:40 GMT', 'expires_timestamp': 1706257000, 'domain': '.facebook.com', 'path': '/', 'secure': True, 'httponly': True, 'samesite': 'None'}, {'name': 'datr', 'value': 'aMM8Zb2qBmtztvpdwwrykC6-', 'expires': 'Sun, 01 Dec 2024 08:16:40 GMT', 'expires_timestamp': 1733041000, 'domain': '.facebook.com', 'path': '/', 'secure': True, 'httponly': True, 'samesite': 'None'}]}}
```
Or if the login fails, it will return the following result:
```python
{'error': {'title': 'Wrong Credentials', 'description': 'Invalid username or password', 'error_subcode': 1348131, 'error_code': 401, 'fbtrace_id': 'AQ1wRUfc-SJoGJ4m4iXGy1B'}}
```
If the login is successful, please call the `success` key and go to `setCookies` to retrieve the Cookie and use it for various features of **fbchat-v2**.

If error, you can view the login error details through the `error` key and call `description`. Below is the **example code**:
```python
if resultLogin.get('success') is None:
     raise SystemExit(f"Error login: {resultLogin['error']['description']} | Error code: {resultLogin['error']['error_code']}")
setCookies = resultLogin['success']['setCookies']
print("Login successful IDFB: {setCookies.split('c_user=')[1].split(';')[0]}")
print("My cookie account: {setCookies}")
```

#### 2.Login with CookieFacebook

This is extremely simple, you just need to *pre-login with your Facebook account* in any browser (Chrome, Firefox, ...). Next, press `F12` to open **DevTools**, and `F5` to refresh the page. A series of Facebook requests will appear, you just need to select any request => Choose the `headers` section of that request. Scroll to find the **Cookie**, then copy them and create them as a variable in **your code**:
```python
setCookies = "c_user=61551671683861; xs=8:51DRVMpDOm...[...]"
```

<a name="checkCookie"></a>
### How to check Live/Die cookie?

This is very simple. Facebook always has data (**fb_dtsg**, **jazoest**, ...) sent to *graphql*. If you can obtain. obtain this data => Your Cookie is *working*, and versa vice. Below is the **example code**:
```python
getData = __facebookToolsV2.dataGetHome(setCookies)
try:
     print(f"{getData['FacebookID']} => Cookies is working!")
except:
     raise SystemExit("Cookies is DIE")
```

<a name="receiveThread"></a>
### How to receive message Thread?

Do you want to receive messages from a Thread? You need to have the *ID* of that Thread. Click [here](https://github.com/MinhHuyDev/fbchat-v2/tree/main#c%C3%A1c-c%C3%A2u-h%E1%BB%8Fi-th%C6%B0%E1%BB%9Dng-g%E1%BA%B7p) if you want to know how to get the ThreadID. Below is a **example code** on how to receive messages from the thread:
```python
threadID = 4805171782880318
getMessage = __messageListen.Listen(getData, threadID)
print(getMessage)
```
