def validar_cpf(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit()
