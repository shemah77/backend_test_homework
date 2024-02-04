
import csv

from datetime import datetime as dt

from chardet.universaldetector import UniversalDetector



def chardetection():
    detector = UniversalDetector()
    with open('output.csv', 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result




def readfileFn():
    '''Read csv file and return it as a lines list of Dict, where first line is dict fields '''
    lines = []
    file_date = input("Enter the date of file output.csv\n")
    file_date = dt.strptime(file_date, '%d-%m-%Y')

    with open('output.csv', encoding='windows-1251', newline='') as csvfile:
        # line = csv.reader(csvfile, delimiter=';')
        dic_lines = csv.DictReader(csvfile, delimiter=';')
        dic_lines.fieldnames = ['fn_number', 'in_reestr', 'in_active', 'notes']
        # for row in line:
        #     lines.append(row)

        lines_of_dict = list(dic_lines)
    return file_date, lines_of_dict

def input_data():
    '''input data from file'''

    with open ('fn_s.csv', 'r') as f:
        line = f.readlines()

        return line

def ActivationDate (lines):
    '''ActivationDate from csv file with first line в первой строке csv'''
    Activation_period: list = []
    count = 0
    count1 = 0
    count1_5 = 0
    count5_10 = 0
    count10_20 = 0
    for i in lines:
        if i['ActivationDate'] != '':
            i['ActivationDate'] = dt.strptime(i['ActivationDate'], '%d.%m.%Y')
            Activation_period.append(dt.now() - i['ActivationDate'])
            count += 1
    print(lines)
    print(count)
    print('==============')
    for i in Activation_period:
        if i.days < 3677 and i.days >= 0:
            if i.days < 1:
                count1 += 1
            elif i.days > 1 and i.days < 5:
                count1_5 += 1
            elif i.days > 5 and i.days < 10:
                count5_10 = +1
            elif i.days > 10 and i.days < 20:
                count10_20 = +1
            elif i.days > 20:
                countMore20 = +1

# считаем кол-во активных фн по выходному файлу Сорокина
def active_fn_count(lines):
    count = 0
    count_non = 0
    total = 0
    for i in lines:
        if i['in_active'] == '0':
            count +=1
        elif i['in_active'] == '1':
            count_non += 1
        total +=  1
    return f' активировались  {count},  доля {round(count/total*100,0)} %  не активных {count_non}, всего: {total}'


if __name__ == '__main__':
    # line = input_data()
    file_date, lines = readfileFn()
    count: int = 0
    # print (lines)
    print (f'с даты активации прошло {dt.now() - file_date}')
    print (active_fn_count(lines))
    print (chardetection())
































