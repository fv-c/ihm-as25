import matplotlib.pyplot as plt

sections = [
    "Frase I.1:\nshadow of my broken memories",
    "Frase I.2:\nlike an abandoned queen",
    "Interpolazione 1",
    "Elettronica fissa",
    "Interpolazione 2",
    "Frase I.3:\ndarkness of abandonment"
]

durations = [1.5, 1.5, 1.0, 2.0, 1.0, 1.0]

start_times = [0]
for duration in durations[:-1]:
    start_times.append(start_times[-1] + duration)

colors = [
    "#a6cee3",  # Frase I.1
    "#1f78b4",  # Frase I.2
    "#b2df8a",  # Interpolazione 1
    "#fb9a99",  # Elettronica fissa
    "#b2df8a",  # Interpolazione 2
    "#33a02c"   # Frase I.3
]

output_path = "melologueI-project-map.pdf"

fig, ax = plt.subplots(figsize=(12, 2.5))

for label, start, duration, color in zip(sections, start_times, durations, colors):
    ax.barh(0, duration, left=start, height=0.5, color=color, edgecolor='black')
    ax.text(start + duration / 2, 0, label, va='center', ha='center',
            fontsize=7, weight='bold', rotation=0)

for start in start_times:
    ax.text(start, 0.3, f"{start:.1f}'", ha='center', va='bottom', fontsize=8)

ax.set_xlim(0, sum(durations))
ax.set_xticks(range(0, int(sum(durations)) + 1))
ax.set_xlabel("")  # Nessuna etichetta per l'asse X
ax.get_yaxis().set_visible(False)

plt.tight_layout()
plt.savefig(output_path, format='pdf')
plt.close()
