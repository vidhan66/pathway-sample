FROM pathwaycom/pathway:latest

WORKDIR /app

COPY . . 
CMD [ "python","pathway_app.py" ]