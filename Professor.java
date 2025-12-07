public class Professor extends Usuario {
    public Professor(int id, String nome) {
        super(id, nome, TipoUsuario.PROFESSOR);
    }

    public Tarefa associarTarefa(int disciplinaId, double nota, double peso, TipoTarefa tipo){
        return Tarefa.criar(disciplinaId, nota, peso, tipo);
    }

    public void editarPeso(int TarefaId, double novoPeso){
        Tarefa.editarPeso(tarefaId, novoPeso);
    }
}