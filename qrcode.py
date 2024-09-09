import qrcode

def gerar_qrcode(dados, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)

    print(f'QRCode gerado com sucesso: {nome_arquivo}')

if __name__ == "__main__":
    dados = input("Digite os dados para o QRCode: ")
    nome_arquivo = input("Digite o nome do arquivo de saída (com extensão .png): ")
    gerar_qrcode(dados, nome_arquivo)