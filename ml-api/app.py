import uvicorn, pickle
from fastapi import FastAPI, HTTPException
from pathlib import Path
from dtos.predictDTO import PredictDTO
from dtos.predictResponse import PredictResponse


MODEL_FILE = Path('/app/shared/model.pkl')

app = FastAPI()


@app.post('/model/predict', tags=['model'],
          response_model=PredictResponse, status_code=200)
async def predict(data: PredictDTO):
    if not MODEL_FILE.exists():
        raise HTTPException(status_code=404, detail='Model not found')
    
    data = data.model_dump()

    x = data['x']
    y = data['y']

    model = pickle.load(open(MODEL_FILE, 'rb'))
    pred = model.predict([x])[0]

    return {'prediction': pred}


if __name__ == '__main__':
    uvicorn.run(app, port=5000)