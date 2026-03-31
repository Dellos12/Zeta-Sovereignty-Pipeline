require 'redis'

# Pegamos a URL que o Jenkins injetou
redis_url = ENV.fetch('REDIS_URL', 'redis://redis:6379/1')

# AQUI ESTÁ O SEGREDO: Use "url:" e NÃO "host:"
# O "url:" faz o Ruby entender o protocolo redis://
$redis = Redis.new(url: redis_url) 

begin
  $redis.ping
  puts "📡 [REDIS] Conexão Estabelecida: Hiperplano Ativo."
rescue StandardError => e
  puts "⚠️ [REDIS] Offline: Falha ao conectar em #{redis_url}. Erro: #{e.message}"
end

