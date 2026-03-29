package main

import (
    "context"
    "log"
    "time"

    "github.com/redis/go-redis/v9"
    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/insecure"

    "manifold/transport/resonance" // Pacote gRPC gerado a partir do .proto
    "manifold/transport/server"
)

var ctx = context.Background()

func main() {
    // 1. Conexão com a Válvula de Memória (Redis)
    rdb := redis.NewClient(&redis.Options{Addr: "redis:6379"})
    go server.StartDashboard(rdb)

    // 2. Conexão com o Reator Python (via gRPC)
    conn, err := grpc.Dial("engine_python:10000", grpc.WithTransportCredentials(insecure.NewCredentials()))
    if err != nil {
        log.Fatalf("❌ Falha gRPC: %v", err)
    }
    defer conn.Close()
    client := resonance.NewAuditoriaZetaClient(conn)

    log.Println("🧪 [GO] Reator Conectado. Iniciando Ciclo de Isótopos.")

    // 3. Ciclo de alternância entre BENZENO e PIRIMIDINA
    for {
        // --- FASE: BENZENO (1.2) ---
        rdb.Set(ctx, "manifold:target_zeta", "1.2006931305", 0)
        rdb.Set(ctx, "manifold:current_signature", "BENZENO", 0)

        // Chamada gRPC para enviar salto
        _, _ = client.ConsultarSalto(ctx, &resonance.RequisicaoSalto{
            TokenOrto:        "1",
            TokenPara:        "1",
            Eletronegatividade: 1.2006931305,
        })

        time.Sleep(10 * time.Second)

        // --- FASE: PIRIMIDINA (1.8) ---
        rdb.Set(ctx, "manifold:target_zeta", "1.8005041305", 0)
        rdb.Set(ctx, "manifold:current_signature", "PIRIMIDINA", 0)

        _, _ = client.ConsultarSalto(ctx, &resonance.RequisicaoSalto{
            TokenOrto:        "1",
            TokenPara:        "1",
            Eletronegatividade: 1.8005041305,
        })

        time.Sleep(10 * time.Second)
    }
}

