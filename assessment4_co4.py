
# Assessment-4 (CO4) - Python simulations and graphs
# Install: pip install matplotlib numpy
# NOTE: Simulated/model values are NOT physical Android-device measurements.

import math
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path("assessment4_graphs")
OUT.mkdir(exist_ok=True)

# ------------------------------------------------------------
# PART II - TASK 2: Architecture assumptions vs measured reality
# Models parallel work and thread-creation overhead.
# Assignment assumptions: p=0.8, 4 cores, 100 ms serial time,
# thread overhead=0.15 ms per worker (0.6 ms total).
# ------------------------------------------------------------
p, cores, serial_ms, overhead_per_thread = 0.8, 4, 100.0, 0.15
speedup = 1 / ((1-p) + p/cores)
parallel_ms = serial_ms / speedup + cores*overhead_per_thread
tiny_work_ms = 0.2
tiny_multi_ms = tiny_work_ms/cores + cores*overhead_per_thread
print("\nTASK 2 - PARALLELISM")
print(f"Amdahl speed-up: {speedup:.2f}x")
print(f"Large workload: single={serial_ms:.1f} ms, parallel={parallel_ms:.1f} ms")
print(f"Tiny workload: single={tiny_work_ms:.2f} ms, parallel={tiny_multi_ms:.2f} ms")
print("Break-even ideal task size: 0.80 ms")

work = np.linspace(0.05, 100, 300)
single = work
multi = work/cores + cores*overhead_per_thread
plt.figure()
plt.plot(work, single, label="Single-thread")
plt.plot(work, multi, label="4 threads + overhead")
plt.axvline(0.8, linestyle="--", label="Break-even ≈ 0.8 ms")
plt.xlabel("Workload duration (ms)")
plt.ylabel("Execution time (ms)")
plt.title("Task 2: Threading overhead and break-even")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(OUT/"task2_thread_overhead.png", dpi=160)
plt.close()

# ------------------------------------------------------------
# PART II - TASK 3: Runtime compilation and GC/frame behaviour
# Illustrative relative execution times for a hot CPU workload.
# Actual cold/warm start, ART filter and GC pauses must be measured
# on an emulator/device using the assignment's adb commands.
# ------------------------------------------------------------
filters = ["verify", "speed-profile", "speed"]
runtime_ms = [1000, 250, 160]  # illustrative normalized workload
plt.figure()
plt.bar(filters, runtime_ms)
plt.ylabel("Illustrative CPU workload time (ms)")
plt.title("Task 3: ART compilation-mode comparison (model)")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(OUT/"task3_art_compilation.png", dpi=160)
plt.close()

hz = 60
frame_budget = 1000/hz
draw_ms = 10
gc_pauses = [0, 4, 20]
frame_times = [draw_ms+x for x in gc_pauses]
missed = [max(0, math.ceil(t/frame_budget)-1) for t in frame_times]
print("\nTASK 3 - FRAME / GC MODEL")
for pause, total, drops in zip(gc_pauses, frame_times, missed):
    print(f"GC pause={pause:>2} ms -> frame={total:.2f} ms, missed frames={drops}")
plt.figure()
plt.bar(["No GC pause", "4 ms pause", "20 ms pause"], frame_times)
plt.axhline(frame_budget, color="red", linestyle="--", label="60 Hz budget = 16.67 ms")
plt.ylabel("Total frame time (ms)")
plt.title("Task 3: GC pause versus 60 Hz frame budget")
plt.legend()
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(OUT/"task3_gc_frame_budget.png", dpi=160)
plt.close()

# ------------------------------------------------------------
# PART II - TASK 4: STRIDE security audit model
# Baseline: TLS + pinning, sandbox, Keystore, non-exported component.
# Weakened case: cleartext traffic and no pinning.
# ------------------------------------------------------------
assets = ["Auth token", "Local DB", "API traffic", "Exported activity"]
baseline = [0, 0, 0, 0]  # 0=blocked, 1=exposed
weakened = [0, 0, 1, 0]
print("\nTASK 4 - SECURITY AUDIT")
print("Baseline verdict: PASS (residual risks documented)")
print("Weakened TLS/pinning verdict: FAIL - release blocked")
for a, b, w in zip(assets, baseline, weakened):
    print(f"{a:20s} baseline={'BLOCKED' if b==0 else 'EXPOSED':7s} "
          f"weakened={'BLOCKED' if w==0 else 'EXPOSED'}")
x = np.arange(len(assets))
plt.figure()
plt.bar(x-0.18, baseline, width=0.36, label="Secure baseline")
plt.bar(x+0.18, weakened, width=0.36, label="Cleartext / no pinning")
plt.xticks(x, assets, rotation=15)
plt.yticks([0,1], ["Blocked", "Exposed"])
plt.ylim(0,1.25)
plt.ylabel("Asset exposure")
plt.title("Task 4: STRIDE audit - baseline vs weakened network")
plt.legend()
plt.tight_layout()
plt.savefig(OUT/"task4_security_audit.png", dpi=160)
plt.close()

# ------------------------------------------------------------
# PART II - TASK 5: Power engineering
# DVFS assumptions from assignment: 2 GHz/1.0 V versus
# 1 GHz/0.8 V, fixed task 2e9 cycles.
# Doze illustration: 8-hour idle, sync every 15 min vs four
# maintenance windows at 1,2,4,8 hours.
# ------------------------------------------------------------
f1, v1 = 2.0, 1.0
f2, v2 = 1.0, 0.8
power_ratio = (f2*v2**2)/(f1*v1**2)
time_ratio = f1/f2
energy_ratio = power_ratio*time_ratio
print("\nTASK 5 - DVFS / DOZE MODEL")
print(f"Lower-frequency power ratio: {power_ratio:.2f}")
print(f"Task duration ratio: {time_ratio:.2f}")
print(f"Energy ratio: {energy_ratio:.2f} (36% energy saving)")
naive_wakes = 8*4
doze_wakes = 4
print(f"Naive sync wake-ups={naive_wakes}; Doze windows={doze_wakes}; reduction=87.5%")
plt.figure()
plt.bar(["2 GHz, 1.0 V", "1 GHz, 0.8 V"], [1.0, energy_ratio])
plt.ylabel("Normalized energy for same task")
plt.title("Task 5: DVFS energy comparison")
plt.ylim(0,1.15)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(OUT/"task5_dvfs_energy.png", dpi=160)
plt.close()

plt.figure()
plt.bar(["Every 15 min", "Doze windows"], [naive_wakes, doze_wakes])
plt.ylabel("Wake-ups in 8 hours")
plt.title("Task 5: Doze maintenance-window model")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(OUT/"task5_doze_wakeups.png", dpi=160)
plt.close()

# ------------------------------------------------------------
# PART II - TASK 6: Battery-aware secure field-tracking policy.
# Constants exactly as listed in the assignment (assumed values).
# ------------------------------------------------------------
E_FIX = 0.0005
E_ENC = 0.000005
E_WAKE = {"WIFI":0.10, "LTE":0.40, "NONE":0.0}
E_REC = 0.00002

def battery_state(pct, charging):
    if charging: return "CHARGING"
    if pct >= 50: return "HIGH"
    if pct >= 20: return "MED"
    if pct >= 10: return "LOW"
    return "CRITICAL"

def policy(pct, charging, network, moving, hot=False, saver=False):
    state = battery_state(pct, charging)
    base = {"CHARGING":10, "HIGH":10, "MED":30, "LOW":60, "CRITICAL":120}[state]
    interval = base
    if not moving: interval *= 6
    if hot: interval *= 2
    if saver: interval *= 2
    if network == "NONE":
        upload, wakes = "QUEUE", 0
    elif hot or saver or state in ("LOW","CRITICAL") or (state=="MED" and not moving):
        upload, wakes = "DEFER", 0
    elif network == "WIFI" and charging:
        upload, wakes = "BATCH_5MIN", 12
    else:
        upload, wakes = "BATCH_15MIN", 4
    fixes = 3600/interval
    transmitted_records = fixes if upload.startswith("BATCH") else 0
    energy = fixes*(E_FIX+E_ENC) + wakes*E_WAKE[network] + transmitted_records*E_REC
    return state, interval, fixes, upload, wakes, energy

cases = [
    ("C1 Charging, Wi-Fi, moving", 80, True, "WIFI", True, False, False),
    ("C2 80%, LTE, moving", 80, False, "LTE", True, False, False),
    ("C3 20%, LTE, stationary", 20, False, "LTE", False, False, False),
    ("C4 Saver, 35%, LTE, moving", 35, False, "LTE", True, False, True),
    ("C5 No connectivity, 60%, moving", 60, False, "NONE", True, False, False),
    ("C6 Hot, 70%, LTE, moving", 70, False, "LTE", True, True, False),
]
labels, energies = [], []
print("\nTASK 6 - BATTERY-AWARE POLICY (ASSUMED MODEL VALUES)")
for name, pct, chg, net, moving, hot, saver in cases:
    st, interval, fixes, upload, wakes, energy = policy(pct, chg, net, moving, hot, saver)
    labels.append(name.split()[0])
    energies.append(energy)
    print(f"{name}: state={st}, sample={interval:.0f}s, fixes/h={fixes:.0f}, "
          f"upload={upload}, radio wakes/h={wakes}, encrypted=YES, energy={energy:.4f} mAh/h")

baseline_records = 3600
baseline_energy = baseline_records*(E_FIX+E_ENC+E_REC) + baseline_records*E_WAKE["LTE"]
print(f"Always-on LTE baseline (1 s sampling, one wake/record): {baseline_energy:.2f} mAh/h")
print(f"C2 saving versus baseline: {(1-energies[1]/baseline_energy)*100:.2f}%")
plt.figure(figsize=(9,5))
plt.bar(labels, energies)
plt.ylabel("Assumed energy (mAh/hour)")
plt.title("Task 6: Energy per hour for six policy conditions")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(OUT/"task6_policy_energy.png", dpi=160)
plt.close()

# Batching scalability values from assignment: 100, 1000, 10000 records,
# 90 records per batch and 0.40 mAh radio wake cost.
record_counts = np.array([100, 1000, 10000])
batch_size = 90
wake_cost = 0.40
batched_wakes = np.ceil(record_counts/batch_size)
unbatched_wakes = record_counts
per_record = E_FIX+E_ENC+E_REC
batched_energy = batched_wakes*wake_cost + record_counts*per_record
unbatched_energy = unbatched_wakes*wake_cost + record_counts*per_record
print("\nTASK 6 - BATCHING SCALE")
for n, bw, uw, be, ue in zip(record_counts, batched_wakes, unbatched_wakes,
                              batched_energy, unbatched_energy):
    print(f"{n:5d} records: batched wakes={int(bw):4d}, unbatched wakes={int(uw):5d}, "
          f"batched={be:.3f} mAh, unbatched={ue:.3f} mAh")
plt.figure()
plt.plot(record_counts, batched_energy, marker="o", label="Batched (90 records/batch)")
plt.plot(record_counts, unbatched_energy, marker="o", label="Unbatched")
plt.xlabel("Number of records")
plt.ylabel("Assumed energy (mAh)")
plt.title("Task 6: Batching versus unbatched energy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(OUT/"task6_batching_energy.png", dpi=160)
plt.close()

print(f"\nAll graph PNG files saved in: {OUT.resolve()}")
