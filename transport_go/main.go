package main

import (
    "context"
    "fmt"
    "log"

    "github.com/redis/go-redis/v9"
    "google.golang.org/grpc"
    "google.golang.org/grpc/credentials/insecure"

    "manifold/transport/resonance"
    "manifold/transport/server"
)

var ctx = context.Background()

func main() {
    // 1. Conexão com o Redis (Hiperplano)
    rdb := redis.NewClient(&redis.Options{Addr: "redis:6379"})

    // Iniciamos o Dashboard em uma goroutine
    go server.StartDashboard(rdb)

    // 2. Conexão gRPC com o Reator Python
    conn, err := grpc.Dial("engine_python:10000", grpc.WithTransportCredentials(insecure.NewCredentials()))
    if err != nil {
        log.Fatalf("❌ Falha gRPC: %v", err)
    }
    defer conn.Close()
    client := resonance.NewAuditoriaZetaClient(conn)

    log.Println("🧪 [GO] Motor Sincronizado. Ouvindo Comandos Zeta...")

    // 3. Ouvinte de Comandos (O 3º Colapso)
    pubsub := rdb.Subscribe(ctx, "zeta:user:command")
    defer pubsub.Close()

    for {
        msg, err := pubsub.ReceiveMessage(ctx)
        if err != nil {
            log.Printf("⚠️ Erro no Hiperplano: %v", err)
            continue
        }

        if msg != nil {
            token := msg.Payload
            log.Printf("🚀 DISPARO: %s. Iniciando Dobra ROI 6 -> ROI 2.", token)

            var targetZeta float64
            if token == "BENZENO" {
                targetZeta = 1.2006931305
            } else {
                targetZeta = 1.8005041305
            }

            // 4. CHAMADA gRPC (Alinhada com seu .proto)
            resp, err := client.ConsultarSalto(ctx, &resonance.RequisicaoSalto{
                TokenOrto:          "1",
                TokenPara:          "1",
                Eletronegatividade: float32(targetZeta),
            })

            if err != nil {
                log.Printf("❌ Falha no Manifold: %v", err)
                rdb.Set(ctx, "zeta:soberania:status", "RUPTURA_DETECTADA", 0)
            } else {
                // Sucesso: Mapeando os 3.344851 da imagem
                rdb.Set(ctx, "manifold:target_zeta", fmt.Sprintf("%f", targetZeta), 0)
                rdb.Set(ctx, "manifold:current_signature", token, 0)
                rdb.Set(ctx, "zeta:soberania:status", "SOBERANIA_CONFIRMADA", 0)
                rdb.Set(ctx, "zeta:ricci:pico", fmt.Sprintf("%f", resp.CurvaturaRicci), 0)
                log.Printf("✅ SALTO CONCLUÍDO: %s (Ricci: %v)", resp.ElementoLogico, resp.CurvaturaRicci)
            }
        }
    }
}

