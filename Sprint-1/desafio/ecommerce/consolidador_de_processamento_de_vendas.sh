echo "Relatório Consolidado" >> /home/leticia/ecommerce/relatorio_final.txt

#adicionando cabeçalhos e os conteúdos dos relatórios gerados

for arquivo in /home/leticia/ecommerce/vendas/backup/relatorio*.txt; do
  echo "Relatório do arquivo: $(basename $arquivo)" >> /home/leticia/ecommerce/relatorio_final.txt
  cat $arquivo >> /home/leticia/ecommerce/relatorio_final.txt
  echo -e "\n" >> /home/leticia/ecommerce/relatorio_final.txt
done
