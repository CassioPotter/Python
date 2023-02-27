import speedtest #pip install speedtest-cli

test=speedtest.Speedtest()

down=test.download()
up=test.upload()

print(f'Velocidade download {down}')
print(f'Velocidade upload {up}')