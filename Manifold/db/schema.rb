# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[8.1].define(version: 2026_03_28_203803) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "pg_catalog.plpgsql"

  create_table "auditoria_zeta", force: :cascade do |t|
    t.string "conjuncao_logica"
    t.datetime "created_at", null: false
    t.string "diagnostico"
    t.string "equacao_estado"
    t.float "gradiente_ricci_observado"
    t.float "similaridade_fase"
    t.string "soberania_veredito"
    t.string "status_compliance"
    t.datetime "updated_at", null: false
  end

  create_table "elemento_zeta", force: :cascade do |t|
    t.float "coeficiente_zeta_alvo"
    t.datetime "created_at", null: false
    t.string "estabilidade"
    t.string "nome"
    t.integer "numero_atomico"
    t.boolean "ressonancia_huckel"
    t.string "simbolo"
    t.datetime "updated_at", null: false
  end
end
