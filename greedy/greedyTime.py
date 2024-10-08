from itertools import permutations

# Fungsi untuk menghitung total waktu pelayanan dari urutan tertentu
def calculate_total_time(order, times):
    T = 0
    cumulative_time = 0
    for customer in order:
        cumulative_time += times[customer - 1]  # Tambah waktu dari pelanggan saat ini
        T += cumulative_time  # Tambah ke total waktu tunggu
    return T

# Fungsi untuk menemukan urutan pelayanan optimal
def find_optimal_order(times):
    customers = [1, 2, 3]
    all_permutations = list(permutations(customers))  # Semua urutan pelanggan
    optimal_order = None
    min_time = float('inf')

    for order in all_permutations:
        total_time = calculate_total_time(order, times)
        if total_time < min_time:
            min_time = total_time
            optimal_order = order

    return optimal_order, min_time

# Data untuk soal (5)
times_5 = [8, 20, 15]
optimal_order_5, min_time_5 = find_optimal_order(times_5)

# Data untuk soal (6)
times_6 = [9, 6, 12]
optimal_order_6, min_time_6 = find_optimal_order(times_6)

# Hasil
print(f"Soal (5) - Urutan optimal: {optimal_order_5}, Total waktu minimum: {min_time_5}")
print(f"Soal (6) - Urutan optimal: {optimal_order_6}, Total waktu minimum: {min_time_6}")
