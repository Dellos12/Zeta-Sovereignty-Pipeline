require 'redis'

# Usamos a REDIS_URL que o Jenkins injetou (redis://redis:6379/1)
# Se não existir, ele tenta o localhost como fallback
redis_url = ENV.fetch('REDIS_URL', 'redis://localhost:6379/0')

$redis = Redis.new(url: redis_url)

# Teste de Conexão no Boot com Retry (Garante que a rede Docker estabilize)
begin
  retries ||= 0
  $redis.ping
  puts "📡 [REDIS] Conexão Estabelecida: Hiperplano Ativo em #{redis_url}"
rescue StandardError => e
  if (retries += 1) < 3
    sleep 1
    retry
  end
  puts "⚠️ [REDIS] Offline: Falha ao conectar em #{redis_url}. Erro: #{e.message}"
end

