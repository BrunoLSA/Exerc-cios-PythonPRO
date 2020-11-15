import pytest

from spam.enviador_de_email import Enviador, EmailInvalido


def test_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['remetente@email.com', 'foo@bar.com']
)
def test_remetente(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        remetente,
        'destinatario@email.com',
        'assunto',
        'corpo do email'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()

    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'destinatario@email.com',
            'assunto',
            'corpo do email'
        )
        assert remetente in resultado
