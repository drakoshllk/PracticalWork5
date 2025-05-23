str = "abcsdfdsfsdfsd"
if str[:3] == "abc":
    str = "www" + str[3:]
else:
    str += "zzz"