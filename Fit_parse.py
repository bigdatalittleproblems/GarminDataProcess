from fitparse import FitFile
import pandas as pd
import json 

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
        workout = []
        for records in fitfile.get_messages(j):
            r = {}
            for record_data in records:
                r[record_data.name] = record_data.value
                workout.append(r)
                dataOutput.update({j:workout})
        workout=pd.DataFrame(dataOutput[j])
        workout.drop_duplicates(inplace=True)
        dataOutput.update({j:workout})
    return dataOutput


if __name__=='__main__':
    path_to_fit_file=''
    df=fit_parse(path_to_fit_file)
