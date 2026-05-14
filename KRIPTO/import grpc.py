import grpc
from concurrent import futures
import time
import multiprocessing

# --- Simulasi Kompilasi Proto (Biasanya dipisah) ---
# Di dunia nyata, kita menjalankan perintah terminal untuk generate code
# Di sini kita asumsikan kode stub sudah ada atau menggunakan library dinamis

class KalkulatorServicer:
    def Hitung(self, request, context):
        print(f"[SERVER] Menghitung: {request.angka1} {request.operasi} {request.angka2}")
        hasil = 0
        error = ""
        
        if request.operasi == "tambah": hasil = request.angka1 + request.angka2
        elif request.operasi == "kurang": hasil = request.angka1 - request.angka2
        elif request.operasi == "kali": hasil = request.angka1 * request.angka2
        elif request.operasi == "bagi":
            if request.angka2 == 0: error = "Error: Pembagian dengan nol!"
            else: hasil = request.angka1 / request.angka2
        
        return {"hasil": hasil, "pesan_error": error}

# --- SERVER RUNNER ---
def jalankan_server():
    # Ini versi sederhana tanpa file proto fisik untuk contoh cepat
    print("[SERVER] Mesin Kalkulator RPC aktif di port 50051...")
    # (Logika server gRPC asli akan ditaruh di sini)
    time.sleep(10) 

# --- CLIENT RUNNER ---
def jalankan_client():
    time.sleep(2)
    print("[CLIENT] Mengirim angka 10 dan 5 dengan operasi 'kali'...")
    print("[CLIENT] Hasil dari server: 50.0")

if __name__ == "__main__":
    # Karena gRPC setup-nya cukup panjang dengan file proto, 
    # ini adalah representasi alurnya:
    
    p1 = multiprocessing.Process(target=jalankan_server)
    p2 = multiprocessing.Process(target=jalankan_client)
    
    p1.start()
    p2.start()
    
    p2.join()
    p1.terminate()