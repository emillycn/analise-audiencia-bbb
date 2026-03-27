import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. DEFINIÇÃO DO INTERVALO FIXO (21h às 01h)
horarios = pd.date_range("2026-03-19 21:00", "2026-03-20 01:00", freq="15min")

# 2. DADOS SIMULADOS 
busca_terca = [5, 8, 15, 45, 95, 100, 85, 60, 40, 25, 15, 8, 5, 3, 2, 1, 1]
busca_quinta = [4, 7, 12, 40, 88, 92, 75, 50, 35, 20, 12, 6, 4, 2, 1, 1, 1]

# 3. CONFIGURAÇÃO DA FIGURA E MARGENS
fig, ax = plt.subplots(figsize=(12, 7.5))
fig.subplots_adjust(left=0.08, right=0.95, top=0.72, bottom=0.15)

# 4. PLOTAGEM PADRONIZADA
ax.plot(horarios, busca_terca, label='Terça (Grade Normal)', color='#457B9D', 
         linewidth=3, linestyle='--', alpha=0.6)
ax.plot(horarios, busca_quinta, label='Quinta (Recuperação Pós-Futebol)', color='#E63946', 
         linewidth=4, marker='o', markersize=6, markerfacecolor='white')

# 5. FORMATAÇÃO DO EIXO X
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.xaxis.set_major_locator(mdates.HourLocator())

# 6. TÍTULOS 
plt.suptitle('Recuperação de faixa: impacto de audiência pós-futebol', 
             fontsize=18, fontweight='bold', color='#1D3557', x=0.08, ha='left', y=0.94)

# O pad=65 empurra o subtítulo para baixo, abrindo espaço para a legenda entre ele e o título principal
ax.set_title('Análise de resiliência: O interesse digital retorna ao padrão normal?', 
             fontsize=12, color='#457B9D', loc='left', pad=65)

# 7. LEGENDA  
# bbox_to_anchor=(0.5, 1.12) centraliza horizontalmente (0.5) acima do gráfico
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05), frameon=False, 
          fontsize=11, ncol=2, columnspacing=2)

# 8. ANOTAÇÃO 
ax.annotate('EFEITO RESSACA\nMesmo com o retorno à grade\nnormal (22:25), o engajamento\né ~8% menor que na terça,\nindicando desgaste do público.', 
             xy=(pd.to_datetime("2026-03-19 22:30"), 92), 
             xytext=(pd.to_datetime("2026-03-19 23:45"), 100),
             fontsize=10, fontweight='bold', color='#1D3557',
             bbox=dict(boxstyle='round,pad=0.6', fc='#F8F9FA', ec='#D1D9E6', lw=1),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='#1D3557', lw=1.5))

# 9. FINALIZAÇÃO TÉCNICA E ESTÉTICA
ax.set_ylabel('Intensidade de Busca (0-100)', fontsize=11, color='#1D3557', labelpad=20)
ax.set_xlabel('Horário de Exibição (Brasília)', fontsize=11, color='#1D3557', labelpad=15)
ax.set_ylim(0, 135)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle=':', alpha=0.4)

# Assinatura
plt.figtext(0.95, 0.02, 'Analista: Emilly Cristine | Inteligência de Audiência', 
            fontsize=9, color='#A8DADC', ha='right')

# 10. SALVAMENTO E EXIBIÇÃO
plt.savefig('03_recuperacao_habito_faixa.png', dpi=300)
plt.show()