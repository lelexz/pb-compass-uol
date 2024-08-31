#criando variável com a data atual
data_atual=$(date +%Y%m%d)

#criando o diretório vendas e copiando o arquivo dados_de_vendas.csv para dentro dele
mkdir -p /home/leticia/ecommerce/vendas
cp /mnt/c/Users/Windows/Downloads/dados_de_vendas.csv /home/leticia/ecommerce/vendas/

#criando o diretório backup dentro de vendas e copiando o arquivo .csv
mkdir -p /home/leticia/ecommerce/vendas/backup
cp /home/leticia/ecommerce/vendas/dados_de_vendas.csv /home/leticia/ecommerce/vendas/backup/dados-$data_atual.csv

#renomeando arquivo para backup-dados-<yyyymmdd>
mv /home/leticia/ecommerce/vendas/backup/dados-$data_atual.csv /home/leticia/ecommerce/vendas/backup/backup-dados-$data_atual.csv

#criando relatorio.txt dentro de backup
relatorio="relatorio-$data_atual.txt"
touch /home/leticia/ecommerce/vendas/backup/$relatorio

#informações dentro do relatório
echo "Relatório de Vendas" > /home/leticia/ecommerce/vendas/backup/$relatorio
echo "Data do sistema: $(date '+%Y/%m/%d %H:%M')" >> /home/leticia/ecommerce/vendas/backup/$relatorio
echo "Data do primeiro registro de venda: $(head -n 2 /home/leticia/ecommerce/vendas/dados_de_vendas.csv | tail -n 1 | cut -d ',' -f5)" >> /home/leticia/ecommerce/vendas/backup/$relatorio
echo "Data do último registro de venda: $(tail -n 1 /home/leticia/ecommerce/vendas/dados_de_vendas.csv | cut -d ',' -f5)" >> /home/leticia/ecommerce/vendas/backup/$relatorio
echo "Qtd total de itens diferentes vendidos: $(cut -d ',' -f2 /home/leticia/ecommerce/vendas/dados_de_vendas.csv | tail -n +2 | sort | uniq | wc -l)" >> /home/leticia/ecommerce/vendas/backup/$relatorio

#mostrar as 10 primeiras linhas e incluir no relatorio.txt
echo "Primeiras 10 linhas do arquivo:" >> /home/leticia/ecommerce/vendas/backup/$relatorio
head -n 10 /home/leticia/ecommerce/vendas/backup/backup-dados-$data_atual.csv >> /home/leticia/ecommerce/vendas/backup/$relatorio

#comprimindo o arquivo backup-dados
zip /home/leticia/ecommerce/vendas/backup/backup-dados-$data_atual.zip /home/leticia/ecommerce/vendas/backup/backup-dados-$data_atual.csv

#apagando arquivos
rm /home/leticia/ecommerce/vendas/backup/backup-dados-$data_atual.csv
rm /home/leticia/ecommerce/vendas/dados_de_vendas.csv
