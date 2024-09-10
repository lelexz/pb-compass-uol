SELECT d.cddep, d.nmdep, d.dtnasc, sum(vd.qtd * vd.vrunt) as valor_total_vendas
from tbdependente d
join tbvendedor v on d.cdvdd = v.cdvdd 
join tbvendas vd on vd.cdvdd = v.cdvdd
where LOWER(status) = LOWER('concluído')
group by d.cddep 
having sum(vd.qtd * vd.vrunt) > 0
order by valor_total_vendas 
limit 1



