SELECT au.nome
FROM autor AS au
LEFT JOIN livro AS liv ON au.codautor = liv.autor 
LEFT JOIN editora AS edi ON liv.editora = edi.codeditora
WHERE edi.endereco NOT IN (SELECT codendereco FROM endereco WHERE estado IN ('PARANÁ', 'RIO GRANDE DO SUL'))
GROUP BY au.nome
ORDER BY au.nome 

	


