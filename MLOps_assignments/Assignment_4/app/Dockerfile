FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY HR_DB model.pkl app.py /app/
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]