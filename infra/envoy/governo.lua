local M = {}
local TARGETS = { benzeno = 1.2006931305, pirimidina = 1.8005041305, tolerance = 0.001 }

M.resolver = function(val)
    if not val or val == 0 then 
        return 1, "❌ VÁCUO_DETECTADO: O reator não emitiu massa." 
    end
    
    local diff_benzeno = math.abs(val - TARGETS.benzeno)
    local diff_py = math.abs(val - TARGETS.pirimidina)

    if diff_benzeno < TARGETS.tolerance then 
        return 0, "✅ SOBERANO_1.2: Geometria de Ricci Estável." 
    elseif diff_py < TARGETS.tolerance then 
        return 0, "✅ DERIVA_1.8: Ressonância Heterocíclica Detectada." 
    else 
        return 1, "❌ RUPTURA: Gradiente " .. val .. " fora da Norma ABNT." 
    end
end

-- Interface de Execução para o Jenkins
local valor_input = arg[1] and tonumber(arg[1]) or 0
local status, msg = M.resolver(valor_input)
print(msg)
os.exit(status)

