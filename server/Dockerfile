FROM  python:bullseye
WORKDIR /app/ 
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY server_handler.py data_methods.py logger_hand.py .env.secret /app/
COPY static/index.html /app/static/