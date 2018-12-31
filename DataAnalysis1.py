import re
import pandas as pd
import datetime
from pandas import ExcelWriter as EW

def log_message(lines, initChar, endChar, lineno):
    startmessage = False
    message = ""

    """ iterate through log lines to get messages
        check if the line contains [[ inicating start of multi line message 
    """
    for i,l in list(enumerate(lines[lineno:])):
        if l.find("[[") == -1 and startmessage is False:
            message = l
            index  = i
            break
        elif l.find("[[") != -1:
            message = message + l
            startmessage = True
        elif l.find("]]") == -1 and startmessage is True:
            message = message + l
        elif l.find("]]") != -1 and startmessage is True:
            startmessage = False
            message = message + l
            index = i
            break
        else:
            pass

    payload = (message, index + 1)
    return payload

def log_parse(logfilepath, excelfilepath, stringsearch, stringenddelimiter, datesearch, startmessagedelimiter, endmessagedelimiter):
    print("Start of parsing at ", datetime.datetime.now())
    try:
        f = open(logfilepath)
        lines = f.readlines()
        messages = []
        lineno = 0
        # m = log_message(lines, "[[", "]]", 1)
        # print(m)
        # print("0",lines[0])
        # print("1",lines[1])
        # print("2",lines[2])
        # print("3",lines[3])
        # print("4",lines[4])
        # print("5",lines[5])
        # print("6",lines[6])
        while lineno < len(lines):
            m = log_message(lines, startmessagedelimiter, endmessagedelimiter, lineno)
            lineno = lineno + m[1]
            # print(m[0])
            searchedstrings = {}
            for index, str in list(enumerate(stringsearch)):
                k, j = 0, 0
                searchstr = str
                searchstrend = stringenddelimiter[index]
                k = m[0].find(searchstr)
                j = m[0][k:].find(searchstrend)
                j = k + j
                # print(k,j)
                if k > 0 and j > 0:
                    strvalue = m[0][k + len(searchstr):j]
                    # print(k, j,userid)
                else:
                    strvalue = ''
                    # print(k,j,'nouser')
                searchedstrings.update({searchstr: strvalue})
            message = {'executiondate': m[0][1:11], 'message': m[0]}
            message.update(searchedstrings)
            messages.append(message)
        #print(messages)
        print("Total no of messages parsed ", len(messages))
       # messages = messages.append({'executiondate':datetime.datetime.now(),'testcol':'Test'})
        raise()
    except Exception as e:
        print("End of parsing at ", datetime.datetime.now())
        f.close()

        df = pd.DataFrame(messages)
        df = df[df['SAW_SRC_PATH=']!=''][['SAW_SRC_PATH=','executiondate','message','username: ']]
        writer = EW(excelfilepath)
        df.to_excel(writer, "sheet1")
        writer.save()


if __name__ == "__main__":
    INPUT_LOG_PATH = r"C:\Users\Sristi Raj\Downloads\obis1-query.log"
    OUTPUT_PATH = r"C:\Users\Sristi Raj\Desktop\obis1-query_12\output.xlsx"
    log_parse(INPUT_LOG_PATH, OUTPUT_PATH, [r'username: ', r'SAW_SRC_PATH='], [r']', r';'], r'\[dd-dd-dd\].', '[[', ']]')
