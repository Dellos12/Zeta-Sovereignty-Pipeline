require 'redis'

# O cifrão ($) torna a variável global para todo o Rails
$redis = Redis.new(host: ENV.fetch('REDIS_HOST', 'localhost'), port: 6379, db: 0)

# Teste de Conexão no Boot
begin
  $redis.ping
  puts "📡 [REDIS] Conexão Estabelecida: Hiperplano Ativo."
rescue StandardError => e
  puts "⚠️ [REDIS] Offline: Verifique se o container 'redis' está UP."
end

