from flask.testing import FlaskClient

def valid_user_data(name: str = "alice") -> dict:
    return {
        'name': name,
        'email': f'{name.split()[0]}@email.com',
        'password': f'password_{name.split()[0]}_123'
    }

def test_get_register_page(client: FlaskClient):
    # US-002: Página de criação de usuário existe
    response = client.get('/register')
    assert response.status_code == 200

def test_post_register_success(client: FlaskClient):
    # US-002: Criação de usuário válido é bem sucedida
    response = client.post('/register', data=valid_user_data(), 
                           follow_redirects=True) # seguir redirect 
    assert response.status_code == 200

def test_post_register_error_handles_status_400(client: FlaskClient):
    # US-002 Fail: tenta usar um email duplicado
    client.post('/register', data=valid_user_data()) 
    # Segunda tentativa deve dar erro 400 
    response = client.post('/register', data=valid_user_data())
    assert response.status_code == 400
