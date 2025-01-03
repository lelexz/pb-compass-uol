SELECT vendedor.cdvdd, vendedor.nmvdd
FROM tbvendedor as vendedor
left join tbvendas as vendas on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendas.cdvdd
ORDER BY count(vendas.cdven) desc
limit 1







