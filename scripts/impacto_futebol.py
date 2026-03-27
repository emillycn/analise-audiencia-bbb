import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. DADOS
horarios = pd.date_range("2026-03-18 21:00", "2026-03-19 01:00", freq="30min")
busca_terca = [10, 15, 25, 80, 100, 95, 70, 40, 20] 
busca_quarta = [5, 8, 10, 12, 15, 40, 90, 100, 85]

# 2. CONFIGURAÇÃO DA FIGURA
fig, ax = plt.subplots(figsize=(12, 7.5)) 
# Ajuste de margens: abrimos mais espaço no topo (0.75) para a "zona de títulos"
fig.subplots_adjust(left=0.08, right=0.95, top=0.75, bottom=0.15)

# 3. PLOTAGEM
ax.plot(horarios, busca_terca, label='Terça (Grade Normal)', color='#457B9D', 
         linewidth=3, linestyle='--', alpha=0.6)
ax.plot(horarios, busca_quarta, label='Quarta (Pós-Futebol)', color='#E63946', 
         linewidth=4, marker='o', markersize=6, markerfacecolor='white')

# 4. TÍTULOS 
plt.suptitle('O impacto da grade flutuante', 
             fontsize=18, fontweight='bold', color='#1D3557', x=0.08, ha='left', y=0.94)
ax.set_title('Como o atraso da programação devido ao futebol desloca o pico de buscas digital.', 
             fontsize=12, color='#457B9D', loc='left', pad=60) # Pad maior para a legenda caber embaixo

# 5. LEGENDA 
# loc='lower center' + bbox_to_anchor=(0.5, 1.02) coloca ela exatamente acima do quadro do gráfico
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05), frameon=False, 
          fontsize=11, ncol=2, columnspacing=2)

# 6. ANOTAÇÃO 
ax.annotate('DESLOCAMENTO DE PICO\nO interesse máximo migra de\n23:00 para 23:30 acompanhando\no atraso da grade na TV.', 
             xy=(pd.to_datetime("2026-03-18 23:30"), 100), 
             xytext=(pd.to_datetime("2026-03-18 21:15"), 105),
             fontsize=10, fontweight='bold', color='#1D3557',
             bbox=dict(boxstyle='round,pad=0.6', fc='#F8F9FA', ec='#D1D9E6', lw=1),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.15', color='#1D3557', lw=1.5))

# 7. FINALIZAÇÃO E EIXOS
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.xaxis.set_major_locator(mdates.HourLocator())
ax.set_ylabel('Intensidade de Busca (0-100)', fontsize=11, color='#1D3557', labelpad=20)
ax.set_xlabel('Horário de Exibição (Brasília)', fontsize=11, color='#1D3557', labelpad=15)
ax.set_ylim(0, 120)

# Estética Clean
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle=':', alpha=0.4)

plt.figtext(0.95, 0.02, 'Analista: Emilly Cristine | Projeto Audiência Globo', 
            fontsize=9, color='#A8DADC', ha='right')

plt.savefig('01_impacto_grade_final.png', dpi=300)
plt.show()