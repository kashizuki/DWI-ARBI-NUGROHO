while True:
    try:
        bulan = int(input("Masukkan bulan (1-12): "))
        tahun = int(input("Masukkan tahun: "))

        if bulan < 1 or bulan > 12:
            print("Bulan tidak ada. Masukkan angka antara 1 dan 12.")

        # This if statement was incorrectly indented
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            kabisat = True
        else:
            kabisat = False

        if bulan in [1,3,5,7,8,10,12]:
            hari = 31
        elif bulan in [4,6,9,11]:
            hari = 30
        elif bulan == 2:
            hari = 29 if kabisat else 28

        print("bulan", bulan, "tahun", tahun, "memiliki", hari, "hari")
        break

    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")