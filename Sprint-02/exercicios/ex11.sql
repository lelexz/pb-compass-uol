SELECT cdcli, nmcli, sum(qtd * vrunt) as gasto
from tbvendas 
where LOWER(status) = LOWER('concluído') 
group by cdcli
order by gasto desc
limit 1



