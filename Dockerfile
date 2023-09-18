FROM python:3.9
WORKDIR /stream
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir altair==4.1.0
COPY . .
CMD ["streamlit", "run", "stream.py"]
