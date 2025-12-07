public class Professor extends Usuario {
    public Professor(int id, String nome) {
        super(id, nome, TipoUsuario.PROFESSOR);
    }

    public Atividade associarTarefa(int disciplinaId, double nota, double peso, TipoAtividade tipo){
        return Atividade.criar(disciplinaId, nota, peso, tipo);
    }

    public void editarPeso(int atividadeId, double novoPeso){
        Atividade.editarPeso(atividadeId, novoPeso);
    }
}