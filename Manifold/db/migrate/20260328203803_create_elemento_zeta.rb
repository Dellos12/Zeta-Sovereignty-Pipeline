class CreateElementoZeta < ActiveRecord::Migration[8.1]
  def change
    create_table :elemento_zeta do |t|
      t.string :nome
      t.string :simbolo
      t.integer :numero_atomico
      t.float :coeficiente_zeta_alvo
      t.string :estabilidade
      t.boolean :ressonancia_huckel

      t.timestamps
    end
  end
end
