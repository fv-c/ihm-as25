import matplotlib.pyplot as plt
from textwrap import wrap
from matplotlib.patches import Patch

# Sezioni con titoli, testi contratti, durate (minuti.frazioni) e colori
sections = [
    ("Frase I.1", "In the shadow of my shattered memories...\n...what was and will never be again.", .75, "#a6cee3"),
    ("Frase I.2", "The wind carries the echo of promises...\n...for a light that has been extinguished.", .75, "#b2df8a"),
    ("Frase I.3", "The walls of my palace...\n...a fragment of happiness now shattered.", .5, "#1f78b4"),
    ("Fixed media", "solo suono /\nnessuna voce", 2.0, "#fb9a99"),
    ("Frase I.4", "Like an abandoned queen...\n...through the columns of my dying kingdom.", 1.0, "#b2df8a"),
    ("Frase I.5", "A lament fills the air...\n...blooming among stones.", 1.5, "#1f78b4"),
    ("Frase I.6", "In the darkness of this abandonment...\n...with or without you.", 1.5, "#33a02c")
]

# Funzione per convertire tempo decimale in minuti e secondi (es. 1.5 -> "1' 30\"")
def format_time_label(time_decimal):
    minutes = int(time_decimal)
    seconds = int(round((time_decimal - minutes) * 60))
    return f"{minutes}' {seconds:02d}\""

# Calcolo degli start times
start_times = [0]
for _, _, dur, _ in sections[:-1]:
    start_times.append(start_times[-1] + dur)

# Legenda
legend_elements = [
    Patch(facecolor="#a6cee3", edgecolor='black', label="Frase I.1 – fragile"),
    Patch(facecolor="#b2df8a", edgecolor='black', label="Frase I.2 / I.4 – transizione, decadenza"),
    Patch(facecolor="#1f78b4", edgecolor='black', label="Frase I.3 / I.5 – intensità, trauma"),
    Patch(facecolor="#fb9a99", edgecolor='black', label="Fixed media – rottura"),
    Patch(facecolor="#33a02c", edgecolor='black', label="Frase I.6 – accettazione, rinascita")
]

# Output path
output_path = "melologueI-project-map.pdf"

# Crea figura
fig, ax = plt.subplots(figsize=(18, 4.6))

# Disegno barre e testi
for (title, text, duration, color), start in zip(sections, start_times):
    ax.barh(0, duration, left=start, height=1.0, color=color, edgecolor='black')
    max_chars = int(duration * 28)
    wrapped_text = "\n".join(wrap(text, max_chars))
    ax.text(start + duration / 2, 0.2, title, ha='center', va='center',
            fontsize=9, weight='bold', color='black')
    ax.text(start + duration / 2, -0.15, wrapped_text, ha='center', va='center',
            fontsize=8, style='italic', color='black')

# Onset temporali sopra ogni rettangolo in formato m' ss"
for start in start_times:
    ax.text(start, 0.52, format_time_label(start), ha='center', va='bottom', fontsize=8)

# Asse X
total_duration = sum([s[2] for s in sections])
ax.set_xlim(0, total_duration)
ax.set_xticks(range(0, int(total_duration) + 1))
ax.set_xticklabels([f"{i}'" for i in range(0, int(total_duration) + 1)])
ax.tick_params(axis='x', bottom=True, labelbottom=True, length=5)

# Asse Y e generale
ax.set_ylim(-0.5, 0.9)
ax.set_yticks([])
ax.set_xlabel("")
ax.grid(False)

# Legenda in alto
ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1),
          ncol=2, fontsize=9, title="Legenda colori", title_fontsize=10, frameon=True)

# Salva PDF
plt.tight_layout()
plt.savefig(output_path, format='pdf')
plt.close()

output_path
