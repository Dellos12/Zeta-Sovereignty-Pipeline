# Atualizado para a versão exigida pelo seu go.mod em 2026
FROM golang:1.25-alpine 

WORKDIR /app

# Dependências de compilação para o gRPC e Músculo C++
RUN apk add --no-cache gcc musl-dev git

# Camada de Dependências (Cache do Docker)
COPY go.mod go.sum ./
RUN go mod download

# Injeção da estrutura de Soberania (main, server, resonance)
COPY . .

# Sincronia de módulos e compilação do ponto de entrada
RUN go mod tidy
RUN go build -o transport_go ./main.go

# Válvula 8080 (Dashboard) e 50051 (gRPC)
EXPOSE 8080 50051

CMD ["./transport_go"]

