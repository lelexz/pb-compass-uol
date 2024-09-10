SELECT estado, ROUND(AVG(qtd * vrunt), 2) as gastomedio 
from tbvendas 
where LOWER(status) = LOWER('concluído') 
group by estado
order by gastomedio desc



