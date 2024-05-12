FROM python:3.12

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir -q --upgrade -r /api/requirements.txt

COPY ./app /api/app

CMD ["fastapi", "run", "app/run_md_to_html.py", "--port", "8000"]