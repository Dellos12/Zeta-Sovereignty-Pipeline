# app/models/elemento_zeta.rb
class ElementoZeta < ApplicationRecord
  # Forçamos o nome da tabela para não haver deriva silábica
  self.table_name = "elemento_zeta"
  
  # O Ponto de Repouso da Pirimidina (1.8) e do Benzeno (1.2)
  validates :simbolo, uniqueness: true
end


