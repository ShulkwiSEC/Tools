import sys
import requests as req
from termcolor import colored
import threading
import time


stuts200 = []
itsdir = []

def Wellcome():
    print(f"\n{colored('Shulkwi', 'red')+colored('SEC', 'green')}\n")
    print(f"{colored('GoodLuck ', 'green')+colored('O_P', 'red')}")


def log(path='',code=''):
    if(code == 200):
        return colored(f'Found: {path} & Status Code: {code}', 'green')
    elif(code == 403):
        return colored(f'Found Unauthorized: {path} & Status Code: {code}', 'yellow')
    elif(code == 500):
        return colored(f'Internal Server Error: {path} & Status Code: {code}', 'red')
    else: 
        return colored(f'Unknow Case: {path} & Status Code: {code}', 'blue')


def cleanurl(website,path):
    if(website.find('.') > website.find('HERE')):
          url = f"{website.replace('HERE', path)}"
    elif(website.find('.') < website.find('HERE')):
      if(website[-5] != '/'):
          url = f"{website.replace('HERE', '/'+path)}"
      elif(website[-5] == '/'):
          url = f"{website.replace('HERE', path)}"
    return url

def splitlist(original_list):
  if len(original_list) < 4:
    raise ValueError("List must contain at least 4 elements")
  elements_per_list = len(original_list) // 4
  list1 = original_list[:elements_per_list]
  list2 = original_list[elements_per_list:elements_per_list * 2]
  list3 = original_list[elements_per_list * 2:elements_per_list * 3]
  list4 = original_list[elements_per_list * 3:]

  return list1, list2, list3, list4

def fuzzer(website,filepath):
    file = filepath
    for path in set(file):
        url = cleanurl(website, path)
        try:
            res = req.get(url, timeout=2)
            content_txt = res.text
        except req.RequestException:
            continue

        if (res.status_code != 404 and 'Not Found' not in content_txt):
            if('Index Of' in content_txt):
                print(colored(f'DirctoryListing in {url}','red'))
                itsdir.append(url)
            if(res.status_code == 302 or '<DOCTYPE>' not in content_txt):
                itsdir.append(url)
            output = log(url, res.status_code)
            stuts200.append(f'FoundUrl {url} With Stuats_Code {res.status_code}')
            print(output)


def fuzzdir(websitedirs, filepath=sys.argv[2]):
    stuts200fordir = []
    for webdir in set(websitedirs):
        print(colored(f'Entering the url {webdir}','yellow'))
        file = filepath
        for path in set(file):
            url = webdir + "/" + path
            try:
                res = req.get(url, timeout=2)
                content_txt = res.text
            except req.RequestException:
                continue
            if (res.status_code != 404 and 'Not Found' not in content_txt):
                output = log(url, res.status_code)
                stuts200.append(f'FoundUrl {url} With Stuats_Code {res.status_code}')
                print(output)
            if(len(itsdir) > 0):
                itsdir.pop(0)


def saveoutput():
    saveable = input(colored('Do You Want To Save Founded urls On File ..? y/n : ', 'green'))
    if saveable == 'y':
        outputpath = input(colored('Enter Path You Want To SAVE it on The Defulte is (fuzzerouput.txt):','green')) or 'fuzzerouput.txt'
        savefile = open(outputpath,'w')
        for url in set(stuts200):
            savefile.write(f"{url}\n")
    elif saveable == 'n':
        print('Okay I will Not Saving it')
def main(mode=''):
 if(mode != 'fuzzdir'):
   file = open(sys.argv[2]).read().split('\n')
   list1, list2, list3, list4 = splitlist(file)
   th1 = threading.Thread(target=fuzzer,args=(sys.argv[1],list1))
   th2 = threading.Thread(target=fuzzer,args=(sys.argv[1],list2))
   th3 = threading.Thread(target=fuzzer,args=(sys.argv[1],list3))
   th4 = threading.Thread(target=fuzzer,args=(sys.argv[1],list4))
   start_time = time.time()
   th1.start()
   th2.start()
   th3.start()
   th4.start()
   th1.join()
   th2.join()
   th3.join()
   th4.join()
   print(colored(f"We Found {len(set(stuts200))} Urls"+'\n', 'red'))
   print(colored(f"We Found {len(set(itsdir))} Dirctory"+'\n', 'red'))
 if(len(set(itsdir)) != 0):
    fuzzdirable = input('Do You Want To Fuzz The Dirctory We Found ...? y/n ')
    if(fuzzdirable == 'y'):
     listdir1, listdir2, listdir3, listdir4 = splitlist(itsdir)
     thdir1 = threading.Thread(target=fuzzdir,args=(listdir1,list1))
     thdir2 = threading.Thread(target=fuzzdir,args=(listdir2,list2))
     thdir3 = threading.Thread(target=fuzzdir,args=(listdir3,list3))
     thdir4 = threading.Thread(target=fuzzdir,args=(listdir4,list3))
     thdir1.start()
     thdir2.start()
     thdir3.start()
     thdir4.start()
     thdir1.join()
     thdir2.join()
     thdir3.join()
     thdir4.join()
 if(len(set(itsdir)) != 0):
     print(f'There Are {len(set(itsdir))} Dirs More btw')
 saveoutput()
 end_time = time.time()
 elapsed_time = end_time - start_time
 print(colored(f'We Found {len(stuts200)} urls on {elapsed_time:.2f} seconds *_*','green'))

Wellcome()
main()