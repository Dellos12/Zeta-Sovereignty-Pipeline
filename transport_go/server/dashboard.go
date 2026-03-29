package server

import (
    "context"
    "fmt"
    "net/http"

    "github.com/redis/go-redis/v9"
)

var ctx = context.Background()

func StartDashboard(rdb *redis.Client) {
    // Rota principal: http://localhost:8080
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        // O Go busca na memória o que o Python e o Ruby decidiram
        zeta, _ := rdb.Get(ctx, "manifold:target_zeta").Result()
        sig, _ := rdb.Get(ctx, "manifold:current_signature").Result()
        
        // Resposta visual em HTML (Estilo Matrix/Terminal)
        w.Header().Set("Content-Type", "text/html")
        fmt.Fprintf(w, `
            <div style="background:#000; color:#00ff41; font-family:monospace; padding:40px; height:100vh;">
                <h1>🧪 TELEMETRIA DE ISÓTOPOS: INTERFACE REAL</h1>
                <hr style="border:1px solid #00ff41;">
                <h2>[ESTADO ATUAL DO MANIFOLD]</h2>
                <p><b>ISÓTOPO INJETADO:</b> %s</p>
                <p><b>GRADIENTE RICCI (1.2/1.8):</b> %s</p>
                <hr style="border:1px solid #00ff41;">
                <p><i>Aguardando Resonância ABNT-ZETA-1200...</i></p>
                <script>setTimeout(function(){ location.reload(); }, 2000);</script>
            </div>
        `, sig, zeta)
    })

    fmt.Println("🌐 [GO SERVER] Dashboard Visual ativo na porta 8080")
    http.ListenAndServe(":8080", nil)
}

