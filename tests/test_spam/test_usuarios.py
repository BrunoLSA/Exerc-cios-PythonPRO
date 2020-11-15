from spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Bruno")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome="Bruno"), Usuario(nome="Juliana")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
