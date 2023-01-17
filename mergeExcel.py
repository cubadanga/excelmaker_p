import os
import pandas as pd
import time
#import datetime
from datetime import date
import shutil
#pd.set_option('display.max_columns', None)
print('파일 합치기를 시작합니다.')

data_file_folder = './excel/'
data_file_folder2 = './소싱리스트/'
tday = date.today()

tday_s = time.strftime('%Y%m%d', time.localtime(time.time()))
def publish_excel(jointype):
    df = []
    for file in os.listdir(data_file_folder):
        if file.endswith('.xlsx') and jointype in file:
            print('Loading file {0}...'.format(file))
            df.append(pd.read_excel(os.path.join(data_file_folder,file)))
    df_master = pd.concat(df, axis=0, ignore_index=True)
    df_master.to_excel('./excel/'+jointype+'_merge_naver_' + tday_s + '.xlsx', index=False)
    return df

def complete_excel(jointype):
    df = []
    for file in os.listdir(data_file_folder2):
        if file.endswith('.xlsx') and jointype in file:
            print('Loading file {0}...'.format(file))
            df.append(pd.read_excel(os.path.join(data_file_folder2,file)))
            shutil.move(data_file_folder2+file, data_file_folder2+'_bak/bakup_'+file)
    df_master = pd.concat(df, axis=0, ignore_index=True)
    df_master.to_excel('./소싱리스트/'+'소싱리스트_naver.xlsx', index=False)
    return df

publish_excel('배포용')
publish_excel('개인용')
publish_excel('소싱정보')
#complete_excel('소싱')
print('파일 합치기 완료! 아무키나 누르면 종료합니다.')
aaa = input()