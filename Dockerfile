FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Tự động chạy lệnh gom file tĩnh, tạo bảng database và chạy server gunicorn
CMD python manage.py collectstatic --noinput && \
    python manage.py migrate --noinput && \
    gunicorn config.wsgi:application --bind 0.0.0.0:10000