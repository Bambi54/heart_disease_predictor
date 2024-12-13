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
    
    data = pd.DataFrame.from_dict(data.model_dump())

    X_test = data.drop(columns=['Target'])

    model = pickle.load(open(MODEL_FILE, 'rb'))
    pred = model.predict([X_test])[0]

    return {'prediction': pred}


if __name__ == '__main__':
    uvicorn.run(app, port=5000)