from pymongo import MongoClient

# Conexão com o MongoDB local
client = MongoClient("mongodb+srv://userTrabalho:6a4e5Uf2htJq4wkg@cluster0.wmkpgm2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Criando banco e coleção
db = client["Cluster0"]
colecao = db["usuarios"]

# Função CREATE
def criar_usuario(nome, idade, email):
    usuario = {"nome": nome, "idade": idade, "email": email}
    resultado = colecao.insert_one(usuario)
    print(f"Usuário criado com id: {resultado.inserted_id}")

# Função READ
def listar_usuarios():
    usuarios = colecao.find()
    for u in usuarios:
        print(u)

# Função UPDATE
def atualizar_usuario(nome, novo_email):
    resultado = colecao.update_one({"nome": nome}, {"$set": {"email": novo_email}})
    if resultado.matched_count > 0:
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

# Função DELETE
def deletar_usuario(nome):
    resultado = colecao.delete_one({"nome": nome})
    if resultado.deleted_count > 0:
        print("Usuário deletado com sucesso!")
    else:
        print("Usuário não encontrado.")

if __name__ == "__main__":
    print("### CRUD MongoDB ###")

    # Exemplo de uso
    criar_usuario("Lucas", 25, "lucas@email.com")
    criar_usuario("Maria", 30, "maria@email.com")

    print("\n-- Usuários cadastrados --")
    listar_usuarios()

    print("\n-- Atualizando Maria --")
    atualizar_usuario("Maria", "novoemail@maria.com")
    listar_usuarios()

    print("\n-- Deletando Lucas --")
    deletar_usuario("Lucas")
    listar_usuarios()
