import matplotlib.pyplot as plt

sections = [
    "Intro elettronica\nfissata",
    "Intro\nstrumentale",
    "Intro\nlive electronics",
    "Melologo I",
    "Cadenza\nfixed media",
    "Melologo II",
    "Cadenza\nlive electronics",
    "Melologo III"
]
durations = [3, 2, 2, 8, 5, 12, 10, 10]

start_times = [0]
for duration in durations[:-1]:
    start_times.append(start_times[-1] + duration)

colors = [
    "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
    "#80b1d3", "#fdb462", "#b3de69", "#fccde5"
]

output_path = "ihm-full-project-map.pdf"

fig, ax = plt.subplots(figsize=(14, 3))

for label, start, duration, color in zip(sections, start_times, durations, colors):
    ax.barh(0, duration, left=start, height=0.5, color=color, edgecolor='black')
    ax.text(start + duration / 2, 0, label, va='center', ha='center',
            fontsize=9, weight='bold', rotation=90)

for start in start_times:
    ax.text(start, 0.3, f"{start}'", ha='center', va='bottom', fontsize=8)

ax.set_xlim(0, sum(durations))
ax.set_xticks(range(0, sum(durations) + 1, 5))
ax.set_xlabel("")  # Nessuna etichetta per l'asse X
ax.get_yaxis().set_visible(False)

plt.tight_layout()
plt.savefig(output_path, format='pdf')
plt.close()
