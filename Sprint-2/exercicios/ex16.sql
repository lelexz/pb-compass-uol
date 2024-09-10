SELECT estado, nmpro, ROUND(AVG(qtd), 4) as quantidade_media
from tbvendas
where LOWER(status) = LOWER('concluído') 
group by estado, nmpro
order by estado, nmpro

