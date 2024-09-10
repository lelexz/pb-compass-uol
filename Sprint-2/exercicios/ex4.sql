SELECT au.nome, au.codautor, au.nascimento, count(liv.cod) AS quantidade
FROM autor AS au
LEFT JOIN livro AS liv 
ON au.codautor = liv.autor
GROUP BY au.nome
ORDER BY nome


	


