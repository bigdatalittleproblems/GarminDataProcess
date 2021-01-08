from fitparse import FitFile
import pandas as pd
import json 
from pathlib import Path
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
    messageFit=['activity','file_id','session','lap','record','device_info','event'
    # ,'segment_lap'
    ]
    for j in messageFit:
        workout = []
        for records in fitfile.get_messages(j):
            r = {}
            for record_data in records:
                print(j)
                r[record_data.name] = record_data.value
                workout.append(r)
                dataOutput.update({j:workout})
        workout=pd.DataFrame(dataOutput[j])
        workout.drop_duplicates(inplace=True)
        dataOutput.update({j:workout})
        # {i:dataOutput[i].to_csv() for i in dataOutput}
    return {'DataFrame':dataOutput, "json":json.dumps({i:dataOutput[i].to_csv() for i in dataOutput})}
def filestoJSON(garminData: Path):
    dir=Path(garminData)
    data={i.stem:fit_parse(str(i)) for i in garminData.iterdir()}
    return data




