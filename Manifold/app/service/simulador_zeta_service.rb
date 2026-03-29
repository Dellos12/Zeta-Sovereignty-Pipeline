class SimuladorZetaService
  def self.injetar_elemento(simbolo)
    elemento = ElementoZeta.find_by!(simbolo: simbolo)
    
    # Injeção na Memória de Curto Prazo
    $redis.set("manifold:target_zeta", elemento.coeficiente_zeta_alvo)
    $redis.set("manifold:current_signature", elemento.simbolo == "Py" ? "PIRIMIDINA" : "BENZENO")
    
    puts "🧪 [SIMULAÇÃO] Injetando #{elemento.nome}..."
    puts "📡 SINAL_ZETA: #{elemento.coeficiente_zeta_alvo} enviado ao Reator."
  end
end

