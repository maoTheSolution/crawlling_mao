import os

# variables
allLibraries = []
targetLibraries = []
target = 'pip3 install '
con = 0

# check all installed pip libraries 
output = os.popen('pip3 list').readlines()

# make them as a list
for each in range(2, len(output)):
    newStr = ''
    for s in output[each]:
        if(s == ' '):
            break
        newStr = newStr + s
    allLibraries.append(newStr)

# make a list of all required libraries that need to be installed 
if('selenium' not in allLibraries):
    targetLibraries.append('selenium')
if('beautifulsoup4' not in allLibraries):
    targetLibraries.append('beautifulsoup4')
if('webdriver_manager' not in allLibraries):
    targetLibraries.append('webdriver_manager')
if('chromedriver_autoinstaller' not in allLibraries):
    targetLibraries.append('chromedriver_autoinstaller')

# upgrade pip
os.system('pip3 install --upgrade pip')


# install libraries with pip
for each in targetLibraries:
    installed = os.system(target+each)
    con = con + installed
    print(each, " is installed")

# check if all successfully installed
if(con == 0):
    print("all installed")
else :
    print("=" * 10)
    print("WARNIGN : THERE WAS AN ERROR IN INSTALLATION.")
    print("="*10)

