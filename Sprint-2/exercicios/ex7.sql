SELECT au.nome
FROM autor AS au
LEFT JOIN livro AS liv ON au.codautor = liv.autor
GROUP BY au.codautor, au.nome
HAVING COUNT(liv.cod) = 0
ORDER BY au.nome;


