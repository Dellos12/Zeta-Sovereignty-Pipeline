# db/seeds.rb
# Lógica de Hibridização: Injetando os 3 estados do Manifold

ElementoZeta.find_or_create_by!(simbolo: "Zz") do |e|
  e.nome = "Carbono Zeta"
  e.numero_atomico = 6
  e.coeficiente_zeta_alvo = 1.2006931305
  e.estabilidade = "CERNE_ESTÁVEL"
  e.ressonancia_huckel = true
end

ElementoZeta.find_or_create_by!(simbolo: "Ph") do |e|
  e.nome = "Fenantreno Lógico"
  e.numero_atomico = 14
  e.coeficiente_zeta_alvo = 2.2006931305
  e.estabilidade = "RUPTURA_DE_GRADIENTE"
  e.ressonancia_huckel = false
end

ElementoZeta.find_or_create_by!(simbolo: "Py") do |e|
  e.nome = "Pirimidina Semântica"
  e.numero_atomico = 7
  e.coeficiente_zeta_alvo = 1.8005041305
  e.estabilidade = "DERIVA_HETEROCÍCLICA"
  e.ressonancia_huckel = true
end

puts "✅ Tabela Periódica Lógica Hibridizada no Rails."

