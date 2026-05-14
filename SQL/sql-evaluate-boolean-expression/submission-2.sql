-- Write your query below
SELECT E.LEFT_OPERAND, E.OPERATOR, E.RIGHT_OPERAND,
    CASE
        WHEN E.OPERATOR = '=' AND LV.VALUE = RV.VALUE THEN 'TRUE'
        WHEN E.OPERATOR = '<' AND LV.VALUE < RV.VALUE THEN 'TRUE'
        WHEN E.OPERATOR = '>' AND LV.VALUE > RV.VALUE THEN 'TRUE'
    ELSE FALSE 
    END AS VALUE
FROM expressions e
JOIN variables lv ON e.left_operand = lv.name
JOIN variables rv ON e.right_operand = rv.name;