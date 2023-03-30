-- Find customers who like to watch drama movies

SELECT DISTINCT cust.customer_id, cust.first_name, cust.last_name
FROM customer cust
         INNER JOIN rental ren ON cust.customer_id = ren.customer_id
         INNER JOIN inventory inv ON ren.inventory_id = inv.inventory_id
         INNER JOIN film fil ON inv.film_id = fil.film_id
         INNER JOIN film_category fca ON fil.film_id = fca.film_id
         INNER JOIN category cat ON fca.category_id = cat.category_id
WHERE cat.name = 'Drama'
ORDER BY cust.customer_id
;

-- Find all the customer's payments which are over their average payment

SELECT pay.payment_id, cust.first_name, cust.last_name, pay.amount
FROM payment pay
         INNER JOIN customer cust ON pay.customer_id = cust.customer_id
WHERE pay.amount > (SELECT AVG(pay1.amount)
                    FROM payment pay1
                    WHERE pay1.customer_id = pay.customer_id);

SELECT cust.first_name,
       cust.last_name,
       COUNT(pt.payment_id) AS CountOfPayment
FROM payment pt
         INNER JOIN customer cust ON pt.customer_id = cust.customer_id
WHERE pt.amount > (SELECT AVG(pt1.amount)
                   FROM payment pt1
                   WHERE pt1.customer_id = pt.customer_id)
GROUP BY cust.first_name, cust.last_name
ORDER BY CountOfPayment DESC;
