SELECT e.codeditora AS CodEditora, e.nome AS NomeEditora, count(*) AS QuantidadeLivros
FROM editora e 
JOIN livro l ON e.codeditora = l.editora 
GROUP BY e.nome
ORDER BY QuantidadeLivros desc
LIMIT 5