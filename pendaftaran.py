import pandas as pd

# Create a dictionary with the data
data = {
    'No': [1, 2, 3],
    'ID PBSI': [None, None, None],
    'ID BWF': [None, None, None],
    'Nama Lengkap': ['Haikal Mahmuda Asyifa Sagala', 'Jesika Marella Syandova Sagala', 'Tracia Sccarlet Cang'],
    'Tempat Lahir': ['Binjai', 'Pematang Siantar', 'Binjai'],
    'Tanggal Lahir': ['26-05-2009', '11-03-1995', '10-01-2007'],
    'Alamat': ['Jl. Danau Laut Tawar No. 3 Lk. II Sumber Muliorejo Kec. Binjai Timur Binjai', 'JI. T. Amir Hamzah Gg. Sulaiman Lk. I Jati Makmur Kec. Binjai Utara Kota Binjai', 'JI. Anggur No. 65 Lk. VII Bandar Senembah Kec. Binjai Barat - Kota Binjai'],
    'Perkumpulan': ['BRAHRANG, BINJAI', 'BRAHRANG, BINJAI', 'BRAHRANG, BINJAI'],
    'Kota/Kabupaten': ['Pengkot Binjai', 'Pengkot Binjai', 'Pengkot Binjai'],
    'Provinsi': ['Sumatera Utara', 'Sumatera Utara', 'Sumatera Utara'],
    'Status': ['REVIEW', 'REVIEW', 'REVIEW'],
    'Action': ['Q', 'Q', 'Q']
}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)