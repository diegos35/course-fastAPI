## install env virtual  
python -m venv nombre_del_entorno

## activate env
source nombre_del_entorno/bin/activate  


## install fastAPI
pip install fastapi

## install uvicorn
pip install uvicorn

## Run 
uvicorn  main:app --reload  
uvicorn  main:app --reload  --port 5000 --host 0.0.0.0