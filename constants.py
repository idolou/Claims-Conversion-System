currency_rate_dict = {"USD": 1, "AUD": 3, "EUR": 2}

data_formartting_dict = {
    ("MyBook", "VISA"): ["%Y-%m-%d", 0.01],
    ("MyBook", "AMEX"): ["%d-%m-%Y", 1],
    ("MyFlight", "VISA"): ["%Y/%m/%d", 0.01],
    ("MyFlight", "AMEX"): ["%d-%m-%Y", 1],
    ("MyShop", "VISA"): ["%Y-%m-%d", 0.01],
    ("MyShop", "AMEX"): ["%d/%m/%Y", 1],
}

error_dict = {
    (10.1, "VISA"): "FRAUD",
    (10.2, "VISA"): "FRAUD",
    (10.3, "VISA"): "FRAUD",
    (10.4, "VISA"): "FRAUD",
    (10.5, "VISA"): "FRAUD",
    (11.1, "VISA"): "AUTHORIZATION",
    (11.2, "VISA"): "AUTHORIZATION",
    (11.3, "VISA"): "AUTHORIZATION",
    (12.1, "VISA"): "PROCESSING_ERROR",
    (12.2, "VISA"): "PROCESSING_ERROR",
    (12.3, "VISA"): "PROCESSING_ERROR",
    (12.4, "VISA"): "PROCESSING_ERROR",
    (12.5, "VISA"): "PROCESSING_ERROR",
    (12.6, "VISA"): "PROCESSING_ERROR",
    (12.7, "VISA"): "PROCESSING_ERROR",
    (13.1, "VISA"): "SERVICE",
    (13.2, "VISA"): "SERVICE",
    (13.3, "VISA"): "SERVICE",
    (13.4, "VISA"): "SERVICE",
    (13.5, "VISA"): "SERVICE",
    (13.6, "VISA"): "SERVICE",
    (13.7, "VISA"): "SERVICE",
    (13.8, "VISA"): "SERVICE",
    (13.9, "VISA"): "SERVICE",
    (30.0, "VISA"): "SERVICE",
    (34.0, "VISA"): "PROCESSING_ERROR",
    (41.0, "VISA"): "SERVICE",
    (53.0, "VISA"): "SERVICE",
    (71.0, "VISA"): "AUTHORIZATION",
    (82.0, "VISA"): "PROCESSING_ERROR",
    (30.0, "AMEX"): "SERVICE",
    (34.0, "AMEX"): "SERVICE",
    (41.0, "AMEX"): "SERVICE",
    (53.0, "AMEX"): "PROCESSING_ERROR",
    (170.0, "AMEX"): "SERVICE",
    (12.5, "AMEX"): "PROCESSING_ERROR",
    (12.6, "AMEX"): "SERVICE",
    (12.7, "AMEX"): "FRAUD",
    (13.1, "AMEX"): "FRAUD",
    (21.0, "AMEX"): "SERVICE",
    (24.0, "AMEX"): "SERVICE",
    (4.0, "AMEX"): "SERVICE",
    (4507.0, "AMEX"): "PROCESSING_ERROR",
    (4512.0, "AMEX"): "PROCESSING_ERROR",
    (4513.0, "AMEX"): "SERVICE",
    (4515.0, "AMEX"): "SERVICE",
    (4521.0, "AMEX"): "AUTHORIZATION",
    (4522.0, "AMEX"): "PROCESSING_ERROR",
    (4523.0, "AMEX"): "PROCESSING_ERROR",
    (4525.0, "AMEX"): "PROCESSING_ERROR",
    (4526.0, "AMEX"): "FRAUD",
    (4527.0, "AMEX"): "FRAUD",
    (4530.0, "AMEX"): "PROCESSING_ERROR",
    (4532.0, "AMEX"): "SERVICE",
    (4534.0, "AMEX"): "FRAUD",
    (4536.0, "AMEX"): "PROCESSING_ERROR",
    (4540.0, "AMEX"): "FRAUD",
    (4544.0, "AMEX"): "SERVICE",
    (4553.0, "AMEX"): "SERVICE",
    (4554.0, "AMEX"): "SERVICE",
    (4750.0, "AMEX"): "SERVICE",
    (4751.0, "AMEX"): "AUTHORIZATION",
    (4752.0, "AMEX"): "PROCESSING_ERROR",
    (4754.0, "AMEX"): "SERVICE",
    (4755.0, "AMEX"): "SERVICE",
    (4758.0, "AMEX"): "PROCESSING_ERROR",
    (4763.0, "AMEX"): "FRAUD",
    (4798.0, "AMEX"): "FRAUD",
    (4799.0, "AMEX"): "FRAUD",
    (59.0, "AMEX"): "SERVICE",
    (6006.0, "AMEX"): "FRAUD",
    (61.0, "AMEX"): "PROCESSING_ERROR",
    (62.0, "AMEX"): "PROCESSING_ERROR",
    (63.0, "AMEX"): "SERVICE",
    (680.0, "AMEX"): "PROCESSING_ERROR",
    (684.0, "AMEX"): "PROCESSING_ERROR",
}
