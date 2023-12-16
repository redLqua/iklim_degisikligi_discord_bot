from flask import Flask , jsonify
import random
app = Flask(__name__)
linkler = [
    "https://ichef.bbci.co.uk/news/640/cpsprodpb/9FF0/production/_110544904_cc_temperatures_ws_640_nc.png" ,
    "https://www.sivilsayfalar.org/wp-content/uploads/2021/06/turkiye-sera-gazi-emisyonu.jpg" , 
    "https://www.verikaynagi.com/wp-content/uploads/2021/05/iklim-deg%CC%86is%CC%A7iklig%CC%86i-11.13.57-1024x614.png" ,
    "https://www.pindactica.de/wp-content/uploads/photo-gallery/07_%C4%B0klim_e%C4%9Frisi_%E2%80%93_CO2_ve_s%C4%B1cakl%C4%B1k.jpg" ,
    "https://anadolubiyocografyasi.com/wp-content/uploads/2020/12/5.png" ,
    "https://w7.pngwing.com/pngs/937/559/png-transparent-global-temperature-record-global-warming-climate-change-global-climate-change-text-ocean-temperature.png" ,
    "https://blog.finanswebde.com/content/images/2019/11/Screenshot_2019-11-27-climatescope-2019-report-en-pdf-1-.png" ,
    "https://www.trthaber.com/dosyalar/images/iklim.jpg" ,
    "https://3.bp.blogspot.com/-vrFEohBaXa8/Uib7k_PVQwI/AAAAAAAAB2w/9TQ-5-bQ_qI/s1600/2450-Temp-sunspot-co2.jpg" ,
    "https://www.41north.com.tr/wp-content/uploads/2020/06/Tablo2.png"

]

@app.route("/")
def iklim_degisikligi():
    resim_linki=random.choice(linkler)
    iklim_degisikligi={
    "by":"denizAtik",
    "url": resim_linki
}
    return jsonify(iklim_degisikligi)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
