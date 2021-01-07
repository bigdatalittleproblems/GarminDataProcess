from fitparse import FitFile
import pandas as pd
import os
import cowsay
import json 

projWD = os.getcwd()
FitDataFiles = os.path.join(projWD, 'garminData')
fitOrg = '2020-07-03-07-07-52.fit'
os.listdir(FitDataFiles)
messageFit=['activity','file_id','session','lap','record']

def fit_parse(fitDir):
    """
    fitDir is the file path to the Fit File to parse.
    Function will return a DataFrame
    """   
    print(f'Running "fit_parse" for: {fitDir}')
    fitfile = FitFile(fitDir)
    dataOutput={}
    workout = []
    messageFit=['activity','file_id','session','lap','record']
    for j in messageFit:
        # r = {}
        workout = []
        for i in fitfile.get_messages(j):
            r = {}
            # workout = []
            # print(i)
            for record_data in i:
                r ={}
                r[record_data.name] = record_data.value
                # print(r)
                workout.append(r)
                dataOutput.update({j:workout})
                # print(workout)
        workout=pd.DataFrame(dataOutput[j])
        dataOutput.update({j:workout})
        
                # workout=pd.DataFrame(workout)
        # print(workout)
    #             workout=pd.DataFrame(workout)
    #             workout.drop_duplicates(inplace=True)
    #             dataOutput.update({j:workout})
    return dataOutput


if __name__=='__main__':
    df=fit_parse('/home/cramirez/garminProj/GarminData/garminData/2020-02-25-05-13-14.fit')
    # print(df)
    # x=df.to_csv()
    # print(df)