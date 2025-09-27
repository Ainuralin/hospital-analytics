SELECT dept_id,
       SUM(CASE WHEN role = 'nurse' THEN 1 ELSE 0 END) AS num_nurses,
       SUM(CASE WHEN role = 'helper' THEN 1 ELSE 0 END) AS num_helpers
FROM (
    SELECT dept_id, 'nurse' AS role FROM nurse
    UNION ALL
    SELECT dept_id, 'helper' AS role FROM helpers
) AS staff
GROUP BY dept_id
ORDER BY dept_id;