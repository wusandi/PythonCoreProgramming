


from urllib import urlretrieve

def firstNonBlock(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
    else:
        return eachLine


def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNonBlock(lines)
    lines.reverse()
    print firstNonBlock(lines)


def download(url='http://www', proccess=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        proccess(retval)


if __name__ == '__main__':
    download()







