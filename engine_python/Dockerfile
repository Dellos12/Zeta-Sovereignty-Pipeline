FROM python:3.10-slim

WORKDIR /app

# Dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    g++ \
    graphviz \
    libgraphviz-dev \
    libgomp1 \
    pkg-config \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

# Variáveis de ambiente
ENV POLARS_SKIP_CPU_CHECK=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Camada 1: Manipulação de Dados
RUN pip install --no-cache-dir \
    pandas \
    "numpy==1.26.4" \
    polars[rtcompat] \
    pyarrow \
    fastparquet \
    tqdm \
    python-dotenv

# Camada 2: Inteligência, Geometria e Linguística
RUN pip install --no-cache-dir \
    # HTTP/2 e transporte
    h11 \
    httpcore \
    httpx \
    # HuggingFace e NLP
    "huggingface-hub[cli]" \
    tokenizers \
    sentencepiece \
    safetensors \
    fsspec \
    datasets \
    accelerate \
    transformers \
    sentence-transformers \
    # Matemática e ML
    scikit-learn \
    joblib \
    threadpoolctl \
    PyYAML \
    regex \
    # Grafos e Geometria
    python-louvain \
    networkit \
    networkx \
    scipy \
    GraphRicciCurvature \
    POT \
    geomstats \
    # Inferência
    onnx \
    onnxruntime \
    "mxnet>=1.9.1" --no-deps \
    # Dependências transitivas críticas
    multiprocess \
    dill \
    xxhash

# Patch MXNet + NumPy
RUN sed -i 's/bool = onp.bool/bool = bool/g' /usr/local/lib/python3.10/site-packages/mxnet/numpy/utils.py || true

# Camada 3: Persistência e gRPC
RUN pip install --no-cache-dir \
    grpcio \
    grpcio-tools \
    protobuf \
    redis \
    psycopg2-binary \
    sqlalchemy \
    pgvector \
    "graphviz>=0.8.1,<0.9.0" \
    "requests>=2.20.0,<3"

# Camada 4: Deep Learning
RUN pip install --no-cache-dir \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY . .

CMD ["python", "main.py"]

