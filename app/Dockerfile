# Imagen y Working DIR
FROM python:3.7-slim
WORKDIR /app 

# Copia de app.py
ADD . /app

# Dependencies
#RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask flask-sqlalchemy pymysql
RUN pip3 install flask flask-sqlalchemy pymysql


# Exponerlo por el p5000
EXPOSE 5000

# launching la app
CMD ["python3", "app.py"]