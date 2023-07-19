import attr

def parse_cookie_string(cookie_string):
     cookie_dict = {}
     cookies = cookie_string.split(";")

     for cookie in cookies:
          if "=" in cookie:
               key, value = cookie.split("=")
          else:
               pass
          try: cookie_dict[key] = value
          except: pass

     return cookie_dict

def Headers(setCookies, dataForm=None):
     headers = {}
     headers["Host"] = "www.facebook.com"
     headers["Connection"] = "keep-alive"
     if (dataForm != None):
          headers["Content-Length"] = str(len(dataForm))
     headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
     headers["Accept"] = "*/*"
     headers["Origin"] = "https://www.facebook.com"
     headers["Sec-Fetch-Site"] = "same-origin"
     headers["Sec-Fetch-Mode"] = "cors"
     headers["Sec-Fetch-Dest"] = "empty"
     headers["Referer"] = "https://www.facebook.com/"
     headers["Accept-Language"] = "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
     
def digitToChar(digit):
          if digit < 10:
               return str(digit)
          return chr(ord("a") + digit - 10)

def str_base(number, base):
     if number < 0:
          return "-" + str_base(-number, base)
     (d, m) = divmod(number, base)
     if d > 0:
          return str_base(d, base) + digitToChar(m)
     return digitToChar(m)

def parse_cookie_string(cookie_string):
     cookie_dict = {}
     cookies = cookie_string.split(";")

     for cookie in cookies:
          if "=" in cookie:
               key, value = cookie.split("=")
          else:
               pass
          try: cookie_dict[key] = value
          except: pass

     return cookie_dict

def dataSplit(string1, string2, numberSplit1, numberSplit2, HTML):
     return HTML.split(string1)[numberSplit1].split(string2)[numberSplit2]
     
def formAll(dataFB, FBApiReqFriendlyName, docID):
     __reg = attr.ib(0).counter
     _revision = attr.ib()
     __reg += 1 
     dataForm = {}
     
     dataForm["fb_dtsg"] = dataFB["fb_dtsg"]
     dataForm["jazoest"] = dataFB["jazoest"]
     dataForm["__a"] = 1
     dataForm["__user"] =str(dataFB["FacebookID"])
     dataForm["__req"] = str_base(__reg, 36) 
     dataForm["__rev"] = dataFB["client_revision"]
     dataForm["av"] = dataFB["FacebookID"]
     dataForm["fb_api_caller_class"] = "RelayModern"
     dataForm["fb_api_req_friendly_name"] = FBApiReqFriendlyName
     dataForm["server_timestamps"] = "true"
     dataForm["doc_id"] = str(docID)
     

     return dataForm
     