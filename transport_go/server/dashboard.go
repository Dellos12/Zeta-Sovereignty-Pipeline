package server

import (
	"context"
	"fmt"
	"net/http"
	"github.com/redis/go-redis/v9"
)

var ctx = context.Background()

func StartDashboard(rdb *redis.Client) {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Lógica de Busca (Input do Usuário)
		if r.Method == http.MethodPost {
			query := r.FormValue("busca_isótopo")
			// Injetamos a intenção de busca no Hiperplano
			rdb.Set(ctx, "manifold:user_query", query, 0)
			rdb.Publish(ctx, "zeta:user:command", query) // Disparo de comando
		}

		zeta, _ := rdb.Get(ctx, "manifold:target_zeta").Result()
		sig, _ := rdb.Get(ctx, "manifold:current_signature").Result()
		status, _ := rdb.Get(ctx, "zeta:soberania:status").Result()

		w.Header().Set("Content-Type", "text/html")
		fmt.Fprintf(w, `
			<body style="background:#000; color:#00ff41; font-family:monospace; padding:40px;">
				<h1>🧪 CONSOLE DE BUSCA ZETA: %s</h1>
				<form method="POST" style="margin-bottom:20px;">
					<input type="text" name="busca_isótopo" placeholder="Digite o Alvo (ex: BENZENO)" 
					       style="background:#000; color:#00ff41; border:1px solid #00ff41; padding:10px; width:300px;">
					<button type="submit" style="background:#00ff41; color:#000; padding:10px; cursor:pointer;">DISPARAR SALTO</button>
				</form>
				<hr style="border:1px solid #00ff41;">
				<div style="border:2px solid #00ff41; padding:20px;">
					<h2>[TELEMETRIA EM TEMPO REAL]</h2>
					<p><b>IDENTIDADE ATUAL:</b> %s</p>
					<p><b>ALVO ZETA:</b> %s</p>
					<p><b>STATUS DE SOBERANIA:</b> <span style="color:#fff; background:red;"> %s </span></p>
				</div>
				<script>setTimeout(function(){ location.reload(); }, 3000);</script>
			</body>
		`, sig, sig, zeta, status)
	})

	fmt.Println("🌐 [GO SERVER] Interface de Busca ativa na porta 8080")
	http.ListenAndServe(":8080", nil)
}

