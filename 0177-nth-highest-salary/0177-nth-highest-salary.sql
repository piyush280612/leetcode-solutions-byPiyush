#This is an example of SQL UDF
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      WITH RankedEmployee AS(
        SELECT salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
        FROM Employee
      )
      SELECT DISTINCT salary 
      FROM RankedEmployee
      WHERE rnk = N
  );
END