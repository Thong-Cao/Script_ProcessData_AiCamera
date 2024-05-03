import pandas as pd
import shutil
import os

"""
## SQL for select event Plate from database

frigate=# \COPY (
SELECT 
    id, 
    start_time, 
    end_time, 
    camera, 
    data->'attributes'->0->'text' as plate 
FROM 
    event 
WHERE 
    label = 'plate' 
    AND data->'attributes'->0->'text' IS NOT NULL
) TO './collected.csv' WITH CSV HEADER;


docker cp 299f42d2b782:./collected.csv/home/pc/aicamera/script_collect/collected.csv
"""

csv_file_path = 'collected.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

source_img = '/home/pc/storage/collect_data/clips/' # Source of folder clips


for i in range(len(df)):

    img_name = df['camera'][i]+'-'+df['id'][i]+'.jpg'
    img_path = source_img + img_name


    new_directory = '/home/pc/aicamera/collect_data4'
    print(df['plate'][i])
    new_filename = str(df['plate'][i]).split('\"')[1] +"_"+str(df['start_time'][i])+ '.jpg'

    # Combine the new directory path with the new filename
    new_path = os.path.join(new_directory, new_filename)
    try:
        # Move the file to the new directory
        shutil.copyfile(img_path, new_path)


    except:
        print("Not found", img_name)
        continue
