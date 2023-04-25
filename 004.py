class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"

class Veiculo:
    def __init__(self, modelo, ano, placa):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def __str__(self):
        return f"Modelo: {self.modelo}\nAno: {self.ano}\nPlaca: {self.placa}"

class Servico:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"Descrição: {self.descricao}\nValor: {self.valor}"

class Peca:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"Descrição: {self.descricao}\nValor: {self.valor}"

class Oficina:
    def __init__(self):
        self.clientes = []
        self.veiculos = []
        self.servicos = []
        self.pecas = []

    def cadastrar_cliente(self, nome, telefone, endereco):
        cliente = Cliente(nome, telefone, endereco)
        self.clientes.append(cliente)

    def cadastrar_veiculo(self, modelo, ano, placa):
        veiculo = Veiculo(modelo, ano, placa)
        self.veiculos.append(veiculo)

    def cadastrar_servico(self, descricao, valor):
        servico = Servico(descricao, valor)
        self.servicos.append(servico)

    def cadastrar_peca(self, descricao, valor):
        peca = Peca(descricao, valor)
        self.pecas.append(peca)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print(veiculo)

    def listar_servicos(self):
        for servico in self.servicos:
            print(servico)

    def listar_pecas(self):
        for peca in self.pecas:
            print(peca)

            class Oficina:
                def __init__(self):
                    self.clientes = []

                def cadastrar_cliente(self, nome, telefone, endereco):
                    cliente = {'nome': nome, 'telefone': telefone, 'endereco': endereco}
                    self.clientes.append(cliente)

                def buscar_cliente(self, nome):
                    for cliente in self.clientes:
                        if cliente['nome'] == nome:
                            return cliente
                    return None

                def listar_clientes(self):
                    for cliente in self.clientes:
                        print(cliente['nome'], cliente['telefone'], cliente['endereco'])


oficina = Oficina()
# cadastra um cliente
oficina.cadastrar_cliente("João da Silva", "(11) 1234-5678", "Rua A, 123")
# cadastra um veículo para o cliente cadastrado acima
oficina.cadastrar_veiculo("Fusca", 1970, "ABC-1234")
# cadastra um serviço

import tkinter as tk
class CadastroCliente:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Cliente")

        self.label_nome = tk.Label(master, text="Nome:")
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)

        self.label_telefone = tk.Label(master, text="Telefone:")
        self.label_telefone.grid(row=1, column=0)

        self.entry_telefone = tk.Entry(master)
        self.entry_telefone.grid(row=1, column=1)

        self.label_endereco = tk.Label(master, text="Endereço:")
        self.label_endereco.grid(row=2, column=0)

        self.entry_endereco = tk.Entry(master)
        self.entry_endereco.grid(row=2, column=1)

        self.button_salvar = tk.Button(master, text="Salvar", command=self.salvar)
        self.button_salvar.grid(row=3, column=0)

    def salvar(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        endereco = self.entry_endereco.get()

        # aqui você pode chamar o método de cadastro de cliente da classe Oficina
        # para adicionar o cliente ao sistema
        print("Cliente cadastrado com sucesso!")
        self.master.destroy()

root = tk.Tk()
app = CadastroCliente(root)
root.mainloop()
