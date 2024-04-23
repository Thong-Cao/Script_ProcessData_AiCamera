import xlsxwriter
import os
import pandas as pd
import re

channel = 'chuyendung'

workbook = xlsxwriter.Workbook(f"{channel}.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write("A1", "id")
worksheet.write("B1", "snapshot")
c = 0
df = pd.read_csv('binhchieu2204.csv')
print(df)
camera_name = 'binhchieu2204'
for i in range(len(df)):
    id = df[0][i]
    index = c
    path = "/home/pc/storage/clips/"
    img = camera_name +'-'+id+'.jpg'
    img_snapshot = path + img
    ocr = df[1][i]

    worksheet.write(f"A{index+2}", ocr)
    worksheet.insert_image(f"B{index+2}", img_snapshot, {"x_scale": 0.3, "y_scale": 0.3})

print("Done!")
print(channel)
workbook.close()