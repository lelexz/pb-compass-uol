SELECT au.codautor, au.nome, count(liv.edicao) AS quantidade_publicacoes
FROM autor AS au
LEFT JOIN livro AS liv ON au.codautor = liv.autor
GROUP BY au.nome 
ORDER BY quantidade_publicacoes DESC 
LIMIT 1
	


