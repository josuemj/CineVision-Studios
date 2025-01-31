#ej 2 a
MERGE (n:Person {born : 1933, name : "Michael Caine"}); 

#ej  3 -> 2 y 3
MATCH (n:Person {name: "Michael Caine", born: 1933})  
RETURN n; 

#ej 2  -> 4
MERGE (a:Person {name: "Michael Caine", born: 1933}) 

MERGE (m:Movie {title: "The Dark Knight", released: 2008}) 

MERGE (a)-[:ACTED_IN]->(m); 

#ej 2  -> 5
MATCH (a:Person {name: "Michael Caine"})-[r:ACTED_IN]->(m:Movie {title: "The Dark Knight"})  

RETURN a, r, m; 

#ej 2  -> 6
MERGE (a:Person {name: "Chadwick Boseman", born: 1976}) 

MERGE (m:Movie {title: "Black Panther", released: 2018}) 

MERGE (a)-[:ACTED_IN]->(m); 

#ej 2  -> 7
MATCH (a:Person {name: "Chadwick Boseman"})-[r:ACTED_IN]->(m:Movie {title: "Black Panther"})  

RETURN a, r, m; 

#ej 2  -> 8
MATCH (a:Person {name: "Emily Blunt"})-[r:ACTED_IN]->(m:Movie {title: "A Quiet Place"}) 
RETURN a, r, m;

#ej 3 -> 1
MERGE (m:Movie {title: "Batman Begins", released: 2005})
MERGE (a:Person {name: "Michael Caine", born: 1933})
MERGE (a)-[r:ACTED_IN {role: "Alfred Pennyworth"}]->(m);

#ej 3 -> 2  

