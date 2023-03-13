FROM python:3.9-slim-buster 

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    bash \
    wget \
    gnupg \
    libgl1-mesa-glx \
    libgconf-2-4 \
    libfontconfig 

EXPOSE 8888

WORKDIR /app

RUN pip install -U pip
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

#CMD ["python"]
#CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='ryang2'"]
CMD ["jupyter", "notebook"]

# docker build --platform linux/X86_64 ds_scrape .
# docker run -it -v "/Users/ruichenyang/projects/bboy_pose:/app" bpose bash 
# docker run -p 8888:8888 -v "/Users/ruichenyang/projects/bboy_pose:/app" -it bpose bash