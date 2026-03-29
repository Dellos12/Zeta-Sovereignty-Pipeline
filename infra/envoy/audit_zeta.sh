#!/bin/bash
echo "🔍 [JENKINS] Iniciando Auditoria de Microestrutura..."

# 1. Teste de Ressonância (Python)
GRADIENTE=$(docker exec engine_python python3 -c "from utils.meta_expert import MetaExpert; print(MetaExpert.calcular_funcao_limite())")

if [[ "$GRADIENTE" == *"1.2006"* ]]; then
    echo "✅ [GEOMETRIA] 1.2 Detectado. Curvatura de Ricci Estável."
else
    echo "❌ [RUPTURA] Gradiente Crítico: $GRADIENTE. Abortando Build."
    exit 1
fi

# 2. Teste de Persistência (Ruby)
STATUS_ABNT=$(docker exec engine_python bundle exec rails runner "puts AuditoriaZeta.last.status_compliance")

if [[ "$STATUS_ABNT" == *"SOBERANIA_CONFIRMADA"* ]]; then
    echo "✅ [GOVERNANÇA] Registro ABNT-ZETA-1200 validado no Hiperplano."
else
    echo "❌ [NÃO-CONFORME] Registro ausente ou corrompido."
    exit 1
fi

