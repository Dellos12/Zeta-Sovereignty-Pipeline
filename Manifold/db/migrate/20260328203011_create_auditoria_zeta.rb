class CreateAuditoriaZeta < ActiveRecord::Migration[8.1]
  def change
    create_table :auditoria_zeta do |t|
      t.string :equacao_estado
      t.string :conjuncao_logica
      t.float :similaridade_fase
      t.float :gradiente_ricci_observado
      t.string :status_compliance
      t.string :diagnostico
      t.string :soberania_veredito

      t.timestamps
    end
  end
end
