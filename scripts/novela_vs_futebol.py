import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. CRIANDO OS HORÁRIOS REAIS (Eixo X)
# Simulando o intervalo das 22:30 às 23:30 (Janela de transição da grade)
horarios = pd.date_range("2026-03-18 22:30", periods=13, freq="5min")

# 2. DADOS 
entrega_futebol = [5, 8, 12, 15, 60, 95, 100, 98, 90, 85, 80, 75, 70]
entrega_novela = [30, 35, 40, 45, 55, 65, 75, 82, 85, 88, 85, 82, 80]

# 3. CONFIGURAÇÃO DA FIGURA
fig, ax = plt.subplots(figsize=(12, 7))
fig.subplots_adjust(left=0.08, right=0.95, top=0.82, bottom=0.15)

# 4. PLOTAGEM COM EIXO DE TEMPO
ax.plot(horarios, entrega_futebol, label='Pós-Futebol (Quarta)', color='#E63946', 
         linewidth=4, marker='o', markersize=8, markerfacecolor='white', markeredgewidth=2)
ax.plot(horarios, entrega_novela, label='Pós-Novela (Quinta)', color='#457B9D', 
         linewidth=3, linestyle='--', alpha=0.7)

# 5. FORMATAÇÃO DO EIXO X 
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M')) # Formato HH:MM
ax.xaxis.set_major_locator(mdates.MinuteLocator(byminute=[0, 15, 30, 45])) # Intervalos de 15 min

# 6. TÍTULOS E ANOTAÇÃO 
plt.suptitle('Análise de Lean-in: Futebol vs. Novela', 
             fontsize=18, fontweight='bold', color='#1D3557', x=0.08, ha='left', y=0.94)
ax.set_title('Comparativo do engajamento inicial do BBB após diferentes programas da grade.', 
             fontsize=12, color='#457B9D', loc='left', pad=25)

# Anotação apontando para o horário real (Ex: 23:00)
pico_hora = horarios[6] # Corresponde às 23:00 no date_range acima
ax.annotate('PICO DE ADRENALINA\nO fim do jogo gera um disparo\nimediato de interesse digital.', 
             xy=(pico_hora, 100), xytext=(pico_hora + pd.Timedelta(minutes=10), 110),
             fontsize=10, fontweight='bold', color='#1D3557',
             bbox=dict(boxstyle='round,pad=0.6', fc='#F8F9FA', ec='#D1D9E6', lw=1),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='#1D3557', lw=1.5))

# 7. ESCALA E PADDING
ax.set_ylabel('Intensidade de Busca (0-100)', fontsize=11, color='#1D3557', labelpad=20)
ax.set_xlabel('Horário de Exibição (Brasília)', fontsize=11, color='#1D3557', labelpad=15)
ax.set_ylim(0, 135)

# Estética Final
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle=':', alpha=0.4)
ax.legend(frameon=False, loc='upper right', bbox_to_anchor=(1, 1.1))

plt.figtext(0.95, 0.02, 'Analista: Emilly Cristine', fontsize=9, color='#A8DADC', ha='right')

plt.savefig('02_comparativo_futebol_novela.png', dpi=300)
plt.show()