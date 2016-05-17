Dari binary ke decimal

| bit 1 | bit 2 | bit 3 | bit 4 | bit 5 | bit 6 | bit 7 | bit 8 |
|-------|-------|-------|-------|-------|-------|-------|-------|
| 128   | 64    | 32    | 16    | 8     | 4     | 2     | 1     |
|1      |1      |0      |0      |1      |0      |0      |0      |


Untuk menterjemahkan binary ke decimal cukup mudah, kita hanya perlu mencari angka 1 (true) dari binary tersebut.
Seperti contoh diatas "11001000". Perhatikan letak bit dan angkanya. Kita lihat bit ke 1 bernilai 1, bit ke 2 bernilai 1, dan bit ke 5 bernilai 1

* bit ke 1 berarti mempunyai nilai 128
* bit ke 2 berarti mempunyai nilai 64
* bit ke 5 berarti mempunyai 8

bit 1 + bit 2 + bit 5 = decimal

128 + 64 + 8 = 200

Contoh:
11010001.00001100.00100010.01001000

* 11010001 = 128 + 64 + 16 + 1 = 209
* 00001100 = 8 + 4 = 12
* 00100010 = 2 + 32 = 34
* 01001000 = 64 + 8 = 72

jadi 209.12.34.72
