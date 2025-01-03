SELECT count(*) AS quantidade, edi.nome, ende.estado, ende.cidade
FROM livro AS liv
LEFT JOIN editora AS edi
ON liv.editora = edi.codeditora 
LEFT JOIN endereco AS ende 
ON edi.endereco = ende.codendereco
GROUP BY nome, estado, cidade
ORDER BY quantidade desc
LIMIT 5


	


