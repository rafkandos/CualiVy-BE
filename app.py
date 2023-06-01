from flask import Flask, request, jsonify
import base64
import mysql.connector
from collections import OrderedDict

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def create_db_connection():
    return mysql.connector.connect(
        host='34.87.156.79',
        user='root',
        password='cualivy123',
        database='cualivydb'
    )

@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        # Membuat koneksi ke database
        conn = create_db_connection()

        # Membuat objek cursor untuk eksekusi query
        cursor = conn.cursor()

        # Mengeksekusi query SELECT untuk mendapatkan data job
        query = "SELECT * FROM Job LIMIT 10"
        cursor.execute(query)

        # Mengambil semua data dari hasil query
        jobs = []
        for row in cursor:
            thirdparty = row[8]
            image = ''
            if thirdparty == 'Kalibrr':
                image = 'https://storage.googleapis.com/logo-detail/jobstreet-logo.png'
            elif thirdparty == 'Glints':
                image = 'https://storage.googleapis.com/logo-detail/glints-logo.png'
            elif thirdparty == 'Jobstreet':
                image = 'https://storage.googleapis.com/logo-detail/jobstreet-logo.png'
            elif thirdparty == 'LinkedIn':
                image = 'https://storage.googleapis.com/logo-detail/linkedin-logo.png'
            elif thirdparty == 'Loker.id':
                image = 'https://storage.googleapis.com/logo-detail/lokerid-logo.jpg'

            job = {
                'guid': row[0],
                'position': row[1],
                'companyname': row[3],
                'location': row[4],
                'notes': row[9],
                'thirdparty': row[8],
                'image': image
            }
            jobs.append(job)

        # Menutup cursor dan koneksi ke database
        cursor.close()
        conn.close()

        # Mengembalikan data dalam format yang diinginkan
        response = OrderedDict()
        response = {
            'status': 200,
            'message': 'Success',
            'data': jobs,
            'totalData': len(jobs)
        }
        return jsonify(response)

    except mysql.connector.Error as error:
        # Menangani kesalahan jika terjadi error pada koneksi atau query
        response = OrderedDict()
        response = {
            'status': 500,
            'message': str(error),
            'data': [],
            'totalData': 0
        }
        return jsonify(response)

@app.route('/searchjobs', methods=['POST'])
def search_jobs():
    try:
        # Mengambil gambar dari body request
        image_data = request.form.get('image')

        # Membuat koneksi ke database
        conn = create_db_connection()

        # Membuat objek cursor untuk eksekusi query
        cursor = conn.cursor()

        # Mengeksekusi query SELECT untuk mendapatkan data job
        query = "SELECT * FROM Job WHERE position LIKE '%" + image_data + "%' LIMIT 10"
        cursor.execute(query)

        # Mengambil semua data dari hasil query
        jobs = []
        for row in cursor:
            thirdparty = row[8]
            image = ''
            if thirdparty == 'Kalibrr':
                image = 'https://storage.googleapis.com/logo-detail/kalibrr-logo.png'
            elif thirdparty == 'Glints':
                image = 'https://storage.googleapis.com/logo-detail/glints-logo.png'
            elif thirdparty == 'Jobstreet':
                image = 'https://storage.googleapis.com/logo-detail/jobstreet-logo.png'
            elif thirdparty == 'LinkedIn':
                image = 'https://storage.googleapis.com/logo-detail/linkedin-logo.png'
            elif thirdparty == 'Loker.id':
                image = 'https://storage.googleapis.com/logo-detail/lokerid-logo.jpg'

            job = {
                'guid': row[0],
                'position': row[1],
                'companyname': row[3],
                'location': row[4],
                'notes': row[9],
                'thirdparty': row[8],
                'image': image
            }
            jobs.append(job)

        # Menutup cursor dan koneksi ke database
        cursor.close()
        conn.close()

        # Mengembalikan data dalam format yang diinginkan
        response = OrderedDict()
        response = {
            'status': 200,
            'message': 'Success',
            'data': jobs,
            'totalData': len(jobs)
        }

    except mysql.connector.Error as error:
        # Menangani kesalahan jika terjadi error pada koneksi atau query
        response = OrderedDict()
        response = {
            'status': 500,
            'message': str(error),
            'data': [],
            'totalData': 0
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()