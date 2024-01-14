## Required
* conda
* docker

## Get started

1. build db server
```
docker-compose up -d
```

2. enter app_server dir
```
cd app_server
```

3. create python venv
```
conda create --name python310_everyones_assistant python=3.10
conda activate python310_everyones_assistant
pip install -r requirements.txt
```

4. create_table
```
python create_tables.py
```

5. build management server
```
streamlit run management_server.py --server.port 50001
```

6. build main server
```
streamlit run main_server.py --server.port 50000
```


## Get restarted
```
execute step 1, 2, 5, 6 of get started.  
```
