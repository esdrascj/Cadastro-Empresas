# Cadastro-Empresas
- Criar um ambiente virtual para rodar o python "python -m venv venv";
- Instalar bibliotecas que serão utilizadas para rodar o programa;
- Bibliotecas: Pyside6, Requests e pandas, openpyxl(extensão pandas para gerar o execel), pyinstaller(para gerar o instalador do programa em python)
- Comandos para converter arquivo qrc. em .py "pyside6-rcc icons.qrc -o icons_rc.py
- Comando para converter arquivo .ui em .py "pyside6-uic cadastro2.ui -o ui_main.py"
- Comando para gerar um único arquivo executavel do programa "pyinstaller.exe --onefile --windowed --icon=icone.ico main.py"
- Criar instalador para windows do aplicativo desktop: https://jrsoftware.org/isdl.php > baixar: innosetup-6.2.2.exe
