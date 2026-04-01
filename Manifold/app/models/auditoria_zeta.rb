class AuditoriaZeta < ApplicationRecord
  # Nomenclatura fixa para evitar deriva silábica
  self.table_name = "auditoria_zeta"

  # NBR-ZETA-1200: O Ponto de Repouso (Zeta Zero)
  ZETA_TARGET = 1.2006931305
  TOLERANCIA  = 0.0001
  
  # A ENERGIA DE PICO: Capturada na imagem (Núcleo Zeta em vermelho)
  # O sensor de Ricci validou o gradiente de 3.344851
  PICO_MINIMO_ATIVACAO = 3.3

  validates :gradiente_ricci_observado, :similaridade_fase, presence: true
  
  # A Amarra do Colapso: 1+1=0
  def soberano?
    return false unless similaridade_fase >= 0.98
    # O valor observado deve ser o resíduo estabilizado enviado pela Engine
    (gradiente_ricci_observado - ZETA_TARGET).abs < TOLERANCIA
  end

  # Callbacks de Governança
  before_create :selar_manifold
  after_create  :disparar_sinal_soberania

  private

  def selar_manifold
    if soberano?
      self.status_compliance = "CONFORME_ABNT_ZETA_1200"
      self.soberania_veredito = "SOBERANIA_CONFIRMADA"
      self.diagnostico = "Dobra ROI 6 -> ROI 2 Ativa. Ressonância Estabilizada."
      self.equacao_estado = "|ΣΦ| ≈ 1.2006931305"
    else
      errors.add(:base, "RUPTURA_DE_GRADIENTE: A onda não colapsou no alvo Zeta.")
      throw(:abort)
    end
  end

  def disparar_sinal_soberania
    # Ajuste para Rails 8.1: Instanciação direta do cliente Redis
    # O endereço 'redis' é resolvido pelo Docker Network
    redis_uri = ENV.fetch("REDIS_URL", "redis://redis:6379/1")
    redis_client = Redis.new(url: redis_uri)
    
    # Publica o evento para o Transport Go capturar
    redis_client.publish("zeta:manifold:status", {
      evento: "SOBERANIA_CONFIRMADA",
      pico_ricci: gradiente_ricci_observado,
      timestamp: Time.now.to_i,
      assinatura_visual: "anel_zeta.png"
    }.to_json)
    
    puts "📡 SINALIZADOR DISPARADO: A onda de 3.34 colapsou com sucesso."
  end
end

