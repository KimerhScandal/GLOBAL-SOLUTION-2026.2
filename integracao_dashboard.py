import json

# Dados simulados e calculados pelo sistema IoT do Centro Comunitário
dados_energia_comunidade = {
    "local": "Centro Comunitário de São Bernardo do Campo",
    "indicadores_mensais": {
        "consumo_baseline_kwh": 1052.4,
        "consumo_atual_rede_kwh": 223.7, 
        "geracao_biogas_kwh": 243.0,
        "participacao_renovavel_pct": 52.0
    },
    "impacto_financeiro": {
        "economia_reais": 704.39
    },
    "impacto_ambiental": {
        "lixo_organico_tratado_kg": 2700,
        "emissoes_evitadas_kg_co2": 499.3
    }
}

# Exportando para consumo do Neighborhood Action Dashboard
payload_dashboard = json.dumps(dados_energia_comunidade, indent=4)
print("Payload pronto para o Dashboard:")
print(payload_dashboard)
