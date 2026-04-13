from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None

    if request.method == "POST":
        try:
            jenis_plastik = request.form.get("jenis_plastik", "").strip()
            harga_per_kg = float(request.form.get("harga_per_kg", 0))
            berat_kg = float(request.form.get("berat_kg", 0))
            biaya_tambahan = float(request.form.get("biaya_tambahan", 0))
            diskon = float(request.form.get("diskon", 0))

            if harga_per_kg < 0 or berat_kg < 0 or biaya_tambahan < 0 or diskon < 0:
                raise ValueError("Nilai tidak boleh negatif.")

            subtotal = harga_per_kg * berat_kg
            total_sebelum_diskon = subtotal + biaya_tambahan
            nilai_diskon = total_sebelum_diskon * (diskon / 100)
            total_akhir = total_sebelum_diskon - nilai_diskon

            hasil = {
                "jenis_plastik": jenis_plastik,
                "harga_per_kg": harga_per_kg,
                "berat_kg": berat_kg,
                "biaya_tambahan": biaya_tambahan,
                "diskon": diskon,
                "subtotal": subtotal,
                "nilai_diskon": nilai_diskon,
                "total_akhir": total_akhir,
            }

        except ValueError:
            error = "Masukkan angka yang valid untuk harga, berat, biaya tambahan, dan diskon."

    return render_template("index.html", hasil=hasil, error=error)


if __name__ == "__main__":
    app.run(debug=True)
