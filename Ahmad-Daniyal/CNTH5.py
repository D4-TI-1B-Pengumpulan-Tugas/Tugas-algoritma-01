
jam = int(input("Durasi Parkir (Jam bulat): "))
if jam <1:
    print("Durasi minimal 1 jam")
else:
    jam_tambahan = jam - 1
    tarif_tambahan = jam_tambahan * 2000
    biaya = 3000 + tarif_tambahan
    print(f"Jam tambahan: {jam_tambahan}")
    print(f"Biaya parkir: Rp {biaya}")