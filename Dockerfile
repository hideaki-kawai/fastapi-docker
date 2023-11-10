FROM python:3.11-buster

# pythonの出力表示をDocker用に調整
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry

# poetryの定義ファイルを存在する場合コピー
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール（pyproject.tomlがすでにある場合）
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# スタートアップスクリプトをコピー
COPY ./start.sh /src/start.sh
RUN chmod +x /src/start.sh

# スタートアップスクリプトをENTRYPOINTに設定
ENTRYPOINT ["/src/start.sh"]
