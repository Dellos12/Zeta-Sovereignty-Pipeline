FROM golang:1.25-alpine

WORKDIR /app

# Músculo C++ para o transporte de alta performance
RUN apk add --no-cache gcc musl-dev git

# Camada de Dependências (Cache do Docker)
COPY go.mod go.sum ./
RUN go mod download

# Injeção de toda a estrutura (main.go + server/ + resonance/)
COPY . .

# Compilação do Binário Sincronizado
RUN go build -o transport_go .

# Válvula 8080 (Visual) e 50051 (Dados)
EXPOSE 8080 50051

CMD ["./transport_go"]

