from app import app, db, User  

                                                #script para limpar todos os usuários cadastrados
def cleanup_users():
    with app.app_context():
        try:
            db.session.query(User).delete()
            db.session.commit()
            print("Todos os usuários foram excluídos com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir usuários: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    cleanup_users()
