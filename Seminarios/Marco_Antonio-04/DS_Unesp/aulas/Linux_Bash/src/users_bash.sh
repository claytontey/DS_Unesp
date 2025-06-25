#!/bin/bash

# Caminho do arquivo de logins
ARQUIVO_LOGINS="logins.txt"

# Criar diretório compartilhado
echo "Criando diretório compartilhado /home/trabalhos..."
sudo mkdir -p /home/trabalhos
sudo chmod 777 /home/trabalhos
echo "Diretório compartilhado pronto."

# Ler e processar cada login do arquivo
while IFS= read -r usuario || [[ -n "$usuario" ]]; do
    echo "Criando usuário: $usuario"
    if id "$usuario" &>/dev/null; then
        echo "Usuário $usuario já existe. Pulando..."
    else
        sudo adduser --disabled-password --gecos "" "$usuario"
        echo "$usuario:123456" | sudo chpasswd
        sudo mkdir -p /home/$usuario
        sudo chown $usuario:$usuario /home/$usuario
        sudo chmod 700 /home/$usuario
        echo "Usuário $usuario criado com sucesso."
    fi
done < "$ARQUIVO_LOGINS"

echo "Todos os usuários foram criados com base no arquivo $ARQUIVO_LOGINS"
echo "O diretório compartilhado /home/trabalhos foi criado com sucesso."