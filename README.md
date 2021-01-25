# Dashboard
Dashboard com Flask e Pusher

# Pré-requisitos
Baixar lib's necessárias

   ```
    pip install -r requirements.txt
   ```

Criar arquivo .env com as seguintes variáveis

   ```
    APP_ID='PUSHER_APP_ID'
    KEY='PUSHER_KEY'
    SECRET='PUSHER_SECRET'
    CLUSTER='PUSHER_CLUSTER'
    SSL=True

    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres_db
    POSTGRES_PORT=5432
    POSTGRES_DB=postgres

    SQLALCHEMY_TRACK_MODIFICATIONS= False
   ```

 # Docker-compose
 para uma visualização rápida, baixar docker-compose e executar o seguinte comando
    
   ```
    docker-compose up
   ```
