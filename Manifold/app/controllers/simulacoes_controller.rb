
class SimulacoesController < ApplicationController
  # Interface de Monitoramento da Ressonância Zeta
  def monitoramento_zeta
    # Captura a última evidência de telemetria enviada pela Engine Python
    @auditoria = AuditoriaZeta.order(created_at: :desc).first

    if @auditoria
      # Valores puros extraídos da imagem (O Pico de 3.344851)
      @ricci_pico = @auditoria.gradiente_ricci_observado
      @ricci_fase = @auditoria.similaridade_fase
      
      # Status derivado da conformidade NBR-ZETA-1200
      @status = @auditoria.status_compliance
      @veredito = @auditoria.soberania_veredito
    else
      render json: { erro: "Aguardando sinal do Hiperplano..." }, status: :no_content
    end
  end
end
