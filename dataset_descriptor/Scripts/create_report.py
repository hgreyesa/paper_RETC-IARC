from dataprep.eda import  plot,create_report
import pandas as pd
import os

in_path = os.environ.get("INPUT_PATH", "/home/input/")
out_path = os.environ.get("OUTPUT_PATH", "/home/output/")
iput_path=f"{in_path}RETC20042022-IARC136.csv"
output_path=f"{out_path}RETC20042022-IARC136_report.html"
#Read data as dataframe
data = pd.read_csv(iput_path, encoding='utf-8', low_memory=False, sep=",")
#Create the dataset report
report = create_report(data, title='Mexican RETC-IARC dataset')
#Save the report
report.save(output_path)