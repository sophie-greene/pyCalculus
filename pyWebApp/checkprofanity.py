#also can use pirate speech
import urllib
def read_txtfile(filename):
    fin = open(filename)
    data = fin.read()
    fin.close()
    print(data)
    return data
# #
def check_profanity(txt):
    # connect to WEBSITE
    con = urllib.urlopen("http://www.wdyl.com/profanity?q=" + txt)
    out = con.read()
    con.close()
    print(out)

    if "true" in out: return True
    elif "false" in out:return False
# if str(out).find("true"): return True
# elif str(out).find("false"):return False

def main():
    filename = "/home/some/off.txt"
    txt = read_txtfile(filename)
    prof = check_profanity(txt)
    if(prof):print("Profanity used!!!!!!!")
main()
