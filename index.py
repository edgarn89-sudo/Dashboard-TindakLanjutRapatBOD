import os
import sys
import subprocess
from flask import Flask

# Ini adalah objek "app" yang dicari-cari oleh Vercel dari kemarin
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # Trik memanggil Streamlit dari dalam fungsi WSGI Vercel
    script_path = os.path.join(os.path.dirname(__file__), '..', 'app.py')
    os.system(f"streamlit run {script_path} --server.port 8080 --server.address 0.0.0.0 &")
    return "Dashboard sedang diinisiasi oleh sistem Vercel... Mohon refresh halaman beberapa saat lagi."