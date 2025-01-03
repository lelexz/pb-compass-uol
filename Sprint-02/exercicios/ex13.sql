SELECT cdpro, nmcanalvendas, nmpro, sum(qtd) as quantidade_vendas
from tbvendas
where LOWER(status) =  LOWER('concluído') and nmcanalvendas in ('Matriz', 'Ecommerce')
group by nmcanalvendas, nmpro 
order by sum(qtd)
limit 10



