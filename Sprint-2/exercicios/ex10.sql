SELECT vndr.nmvdd as vendedor, sum(vendas.qtd * vendas.vrunt) as valor_total_vendas, 
	   ROUND(SUM( vendas.qtd * vendas.vrunt)* vndr.perccomissao / 100, 2) as comissao
from tbvendas as vendas
join tbvendedor as vndr on vendas.cdvdd = vndr.cdvdd 
where LOWER(vendas.status) = LOWER('concluído') 
GROUP by vndr.nmvdd
order by comissao desc




