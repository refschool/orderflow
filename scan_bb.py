from mail_lib import send_mail
import pandas as pd
import numpy as np

# read tsv file
df = pd.read_csv('output.txt')
print(df)

#if True:
#    send_mail('yvon.huynh@gmail.com','from python','content')

