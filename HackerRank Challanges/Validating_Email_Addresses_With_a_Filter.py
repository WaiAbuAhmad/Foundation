def fun(s):
    username=""
    websitename=""
    extention=""
    for i in range(len(s)):
        if s[i] == ".":
            extention = s[i:]
            websitename=s[(len(username)+1):i]
        elif s[i] =="@" :
            username = s[:i]

    if username and extention and websitename and len(extention)<=4 and websitename.isalnum() :
        if  (all((i.isalnum() or i=="-" or i=="_") for i in username)):
            return True
    else:
        return False
        

def filter_mail(emails):