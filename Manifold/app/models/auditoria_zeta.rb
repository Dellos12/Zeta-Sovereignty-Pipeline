# app/models/auditoria_zeta.rb
class AuditoriaZeta < ApplicationRecord
  # Forçamos o Rails a usar o nome correto da tabela criada na migration
  self.table_name = "auditoria_zeta"

  # Parâmetro Científico: O Ponto de Repouso Zeta
  ZETA_TARGET = 1.2006931305
  TOLERANCIA  = 0.0001

  # Auditoria de Soberania (A Válvula NBR)
  def soberano?
    (gradiente_ricci_observado - ZETA_TARGET).abs < TOLERANCIA && similaridade_fase > 0.99
  end

  # Callback para impedir que ruído estatístico (IA Proto) entre no banco
  before_save :validar_conformidade_nbr

  private

  def validar_conformidade_nbr
    unless soberano?
      errors.add(:base, "Ruptura de Gradiente detectada: Não conforme com NBR-ZETA-1200")
      throw(:abort)
    end
  end
end

