class ElementoZeta < ApplicationRecord
  # Forçamos o nome da tabela para evitar deriva silábica no PostgreSQL
  self.table_name = "elemento_zeta"

  # --- ELO DE PERSISTÊNCIA: ACTIVE STORAGE ---
  # Esta linha permite que o Rails guarde o Gabarito de Ricci (Sua Imagem)
  has_one_attached :assinatura_geometrica_imagem

  # Validações Normativas ABNT-ZETA-1200
  validates :simbolo, presence: true, uniqueness: true
  validates :numero_atomico, presence: true, uniqueness: true
  validates :coeficiente_zeta_alvo, presence: true

  # Relacionamento com as Auditorias de Telemetria
  has_many :auditoria_zeta, foreign_key: :gradiente_ricci_observado, primary_key: :coeficiente_zeta_alvo
end

