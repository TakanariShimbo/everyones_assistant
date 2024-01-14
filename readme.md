## Required
* conda
* docker


## Get started
1. create .env
```
duplicate "./db_server/.env_sample" as ".env" in same dir
duplicate "./app_server/model/static/env/.env_sample" as ".env" in same dir
customize yourself
```

2. build db server
```
docker-compose up -d
```

3. enter app_server dir
```
cd app_server
```

4. create python venv
```
conda create --name python310_everyones_assistant python=3.10
conda activate python310_everyones_assistant
pip install -r requirements.txt
```

5. create_table
```
python create_tables.py
```

6. build management server
```
streamlit run management_server.py --server.port 50001
```

7. build main server
```
streamlit run main_server.py --server.port 50000
```


## Get restarted
```
execute step 2, 3, (4), 6, 7 of get started.  
activate only at step 4
```
