-- Write your query below
SELECT E.LEFT_OPERAND, E.OPERATOR, E.RIGHT_OPERAND,
    CASE E.OPERATOR
        WHEN '=' THEN (LV.VALUE = RV.VALUE)
        WHEN '<' THEN (LV.VALUE < RV.VALUE)
        WHEN '>' THEN (LV.VALUE > RV.VALUE)
    END AS VALUE
FROM expressions e
JOIN variables lv ON e.left_operand = lv.name
JOIN variables rv ON e.right_operand = rv.name;