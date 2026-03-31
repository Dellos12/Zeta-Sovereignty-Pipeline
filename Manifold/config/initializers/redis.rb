require 'redis'

# Pega a URL completa do Jenkins ou usa localhost como fallback
redis_url = ENV.fetch('REDIS_URL', 'redis://localhost:6379/0')

# CORREÇÃO CRUCIAL: Use 'url:' para que o Ruby entenda o protocolo redis://
$redis = Redis.new(url: redis_url)

begin
  retries ||= 0
  $redis.ping
  puts "📡 [REDIS] Conexão Estabelecida: Hiperplano Ativo."
rescue StandardError => e
  if (retries += 1) < 3
    sleep 1
    retry
  end
  # Agora o erro mostrará o que realmente falhou
  puts "⚠️ [REDIS] Offline: Verificando infra em #{redis_url}. Erro: #{e.message}"
end

