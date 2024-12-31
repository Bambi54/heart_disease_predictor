import uvicorn, pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from pathlib import Path
from dtos.predictDTO import PredictDTO
from dtos.predictResponse import PredictResponse


MODEL_FILE = Path('/opt/airflow/shared/model.pkl')

app = FastAPI()


@app.post('/model/predict', tags=['model'],
          response_model=PredictResponse, status_code=200)
async def predict(data: PredictDTO):
    if not MODEL_FILE.exists():
        raise HTTPException(status_code=404, detail=f'${MODEL_FILE} not found')
    
    df = pd.DataFrame([data.model_dump(by_alias=True)])
    model = pickle.load(open(MODEL_FILE, 'rb'))
    print(df.head())
    pred = model.predict(df)
    print(pred)

    return {'prediction': pred[0]}


if __name__ == '__main__':
    uvicorn.run(app, port=5000)