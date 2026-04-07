print('Halo, ini ada di dalam dokumen main.py')
print('--------------------')

print('Selamat datang di Pacflix, platform streaming film terbaik!')
print('Apakah Anda ingin melakukan registrasi? (y/n)')
user_input = input().lower()
if user_input == 'y':
    print('Silakan masukkan username: ')
    username = input()
    print('Silakan masukkan password: ')
    password = input()
    print(f'Username: {username}, Password: {password}')
elif user_input == 'n':
    print('Baiklah, silakan jelajahi film-film kami!')
else:
    print('Input tidak valid. Silakan masukkan "y" atau "n".')
print('--------------------')
print('Terima kasih telah menggunakan Pacflix!')
print('--------------------')