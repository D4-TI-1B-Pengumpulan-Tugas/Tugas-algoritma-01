print("=== PROGRAM PARKIR ===")

durasi = int(input("Masukkan durasi parkir (jam): "))

if durasi <= 0:
    print("Durasi tidak valid!")
    print("Durasi parkir minimal 1 jam.")
else:
    tambahan = durasi - 1
    biaya = 3000 + (tambahan * 2000)

    print("Durasi parkir:", durasi, "jam")
    print("Jam tambahan:", tambahan, "jam")
    print("Total biaya: Rp", biaya)