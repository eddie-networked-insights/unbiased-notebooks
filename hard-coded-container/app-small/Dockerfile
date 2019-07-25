FROM tensorflow/tensorflow:1.12.0-devel-gpu-py3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=my-flask-app.py

RUN pip install keras Flask

#user input doesnt work
#CMD ["python3", "load-artifacts-for-inference.py"]

CMD ["flask", "run", "--host=0.0.0.0"]
