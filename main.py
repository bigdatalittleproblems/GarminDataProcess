from fitparse import FitFile
import pandas as pd
import os
from Fit_parse import fit_parse
import cowsay
projWD=os.getcwd()
FitDataFiles=os.path.join(projWD,'garminData')
# fitOrg='2020-07-03-07-07-52.fit'
os.listdir(FitDataFiles)
# os.path.join(FitDataFiles,os.listdir(FitDataFiles)[1])
# x=fit_parse(os.path.join(FitDataFiles,os.listdir(FitDataFiles)[1]))
os.environ.get('USER')

if __name__=='__main__':
    fitDic={}
    for i in os.listdir(FitDataFiles):
        x=fit_parse(os.path.join(FitDataFiles,i))
        if x is None:
            cowsay.beavis(f'Failed for {i}')
            continue
        else:
            y=os.path.join(projWD, 'Output', i.strip(".fit"))
            fitDic.update({y:x})
            x.to_csv(f'{y}.csv')

# fitfile = FitFile(f'./garminData/{fitOrg}')
# for record in fitfile.get_messages('record'):
#     for record_data in record:
#         if record_data.units:
#             print(record_data.name, record_data.value, record_data.units)
#         else:
#             print(record_data.name, record_data.value)
# workout=[]
# for record in fitfile.get_messages('record'):
#     for record_data in record:
#         r = {}
#         for record_data in record:
#             r[record_data.name] = record_data.value
#         workout.append(r)
# df = pd.DataFrame(workout)
# fitOrg.strip('.fit')
# df.columns
# df.heart_rate.max()
# df.to_csv(f'{fitOrg.strip(".fit")}.csv')