public class Administrador extends Usuario {
    public Administrador(int id, String nome) {
        super(id, nome, TipoUsuario.ADMINISTRADOR);
    }

    public Disciplina cadastrarDisciplina(String nome, String codigo) {
        Disciplina disciplina = Disciplina.criar(nome, codigo);
        getDisciplinas().add(disciplina);
        return disciplina;
    }

    public boolean excluirDisciplina(String codigo){
        Disciplina disciplina = Disciplina.buscar(codigo);

        if (disciplina != null){
            Disciplina.excluir(codigo);
            getDisciplinas().remove(disciplina);
            return true;
        } else {
            return false;
        }
    }

}
