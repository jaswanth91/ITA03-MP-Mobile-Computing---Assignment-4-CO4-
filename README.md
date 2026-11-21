# Assessment-4 (CO4) – Mobile Computing
## Python Programs and Graphical Analysis

### 1. Project Description

This project contains Python programs and graphical outputs for the practical tasks in Assessment-4 (CO4) of Mobile Computing.

The project demonstrates Android runtime performance, multithreading, application security, power management, and battery-aware tracking through Python simulations and Matplotlib graphs.

### 2. Objectives

- Analyze multithreading performance and execution overhead.
- Understand Android Runtime (ART) compilation and garbage collection.
- Perform a basic STRIDE security audit.
- Analyze CPU power consumption using DVFS.
- Understand Android Doze mode and wake-up reduction.
- Simulate battery-aware location tracking and data uploading.
- Generate graphical representations of simulation results.

### 3. Software Requirements

| Software / Library | Purpose |
|---|---|
| Python 3.x | Programming language |
| NumPy | Numerical calculations |
| Matplotlib | Graph generation |
| VS Code / PyCharm | Code editor |

### 4. Project Structure

```text
Assessment4_CO4/
│
├── assessment4_co4.py
│
├── assessment4_graphs/
│   ├── task2_thread_overhead.png
│   ├── task3_art_compilation.png
│   ├── task3_gc_frame_budget.png
│   ├── task4_security_audit.png
│   ├── task5_dvfs_energy.png
│   ├── task5_doze_wakeups.png
│   ├── task6_policy_energy.png
│   └── task6_batching_energy.png
│
└── README.md
```

### 5. Installation

Install Python 3.x.

Install the required libraries using:

```bash
pip install numpy matplotlib
```

### 6. Execution

Run the Python program using:

```bash
python assessment4_co4.py
```

The program automatically performs the simulations, displays the calculated results in the terminal, and saves the graphs inside the `assessment4_graphs` folder.

### 7. Task Descriptions

#### Task 2 – Architecture and Multithreading Analysis

- Compares single-threaded and multithreaded execution.
- Uses Amdahl's Law to calculate parallel speed-up.
- Demonstrates thread creation overhead.
- Generates a graph comparing execution time.

#### Task 3 – Runtime Behaviour

- Demonstrates ART compilation modes.
- Analyzes garbage collection pauses.
- Compares frame execution time against a 60 Hz frame budget.
- Generates two graphs.

#### Task 4 – Application Security Audit

- Demonstrates a basic STRIDE security audit model.
- Compares secure and weakened network configurations.
- Identifies possible asset exposure.
- Generates a security comparison graph.

#### Task 5 – Power Management

- Demonstrates Dynamic Voltage and Frequency Scaling (DVFS).
- Compares energy consumption at different CPU frequencies.
- Models Android Doze maintenance windows.
- Generates two graphs.

#### Task 6 – Battery-Aware Field Tracking

- Simulates battery-aware location sampling.
- Considers Wi-Fi, LTE, and unavailable network conditions.
- Models encrypted data queueing and upload batching.
- Calculates energy consumption for six conditions.
- Compares batched and unbatched transmission.
- Generates two graphs.

### 8. Sample Results

| Task | Result |
|---|---|
| Task 2 | 2.5x speed-up |
| Task 3 | 20 ms GC pause exceeds the 60 Hz frame budget |
| Task 4 | Secure baseline: PASS |
| Task 4 | Weakened security: FAIL |
| Task 5 | 36% modeled energy saving using DVFS |
| Task 5 | 87.5% fewer modeled wake-ups using Doze |
| Task 6 | C2 energy consumption: 1.7890 mAh/hour |

### 9. Graphical Outputs

The project generates eight graphs:

1. Threading overhead comparison.
2. ART compilation comparison.
3. Garbage collection and frame budget.
4. Security audit comparison.
5. DVFS energy comparison.
6. Doze wake-up comparison.
7. Battery-aware policy energy consumption.
8. Batched versus unbatched energy consumption.

### 10. Conclusion

This project demonstrates important concepts of mobile computing using Python simulations and graphical analysis.

The results illustrate how multithreading, runtime optimization, application security, power management, and battery-aware tracking can improve mobile application performance and efficiency.

**Note:** The numerical results are simulation outputs based on assumed model parameters. They are not actual measurements from an Android device. Real device measurements require Android Studio, ADB, Perfetto, and Battery Historian.
