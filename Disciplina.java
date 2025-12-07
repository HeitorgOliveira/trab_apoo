public class Disciplina {
    private String nome;
    private String codigo;
    private ArrayList<Tarefa> listaTarefas;

    public String getNome() {
        return nome;
    }


    // Getters e setters gerados pelo Copilot
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public ArrayList<Tarefa> getListaTarefas() {
        return listaTarefas;
    }

    public void setListaTarefas(ArrayList<Tarefa> listaTarefas) {
        this.listaTarefas = listaTarefas;
    }

    public Disciplina(String nome, String codigo){
        this.nome = nome;
        this.codigo = codigo;
        this.listaTarefas = new ArrayList<>();
    }

    public void incluirAtividade(Tarefa tarefa){
        this.listaTarefas.add(tarefa);
        tarefa.setDisciplina(this);
    }

    public double calcularMediaPorTipo(TipoAtividade tipo){
        double somaNotas = 0.0;
        double somaPesos = 0.0;

        for (Tarefa tarefa : listaTarefas) {
            if (tarefa.getTipo() == tipo) {
                somaNotas += tarefa.getNota() * tarefa.getPeso();
                somaPesos += tarefa.getPeso();
            }
        }

        if (somaPesos == 0) {
            return 0.0;
        }

        return Math.round((somaNotas / somaPesos) * 100.0) / 100.0;
    }

    public double calcularMediaFinal(){
        double somaPesos = 0.0;
        double somaNotasPonderadas = 0.0;

        for (Tarefa tarefa : listaTarefas) {
            somaNotasPonderadas += tarefa.getNota() * tarefa.getPeso();
            somaPesos += tarefa.getPeso();
        }

        if (somaPesos == 0) {
            return 0.0;
        }

        return Math.round((somaNotasPonderadas / somaPesos) * 100.0) / 100.0;
    }

    // métodos estáticos para ajduar nas outras chamadas (algumas coisas foram sugeridas pelo gpt)

    public static Disciplina busca(int id){
        if (disciplinas.containsKey(id)){
            return disciplinas.get(id);
        }
        return null;
    }

    public static boolean excluir(int id){
        Disciplina disciplina = Disciplina.buscar(id);
        if (disciplina != null) {
            getDisciplinaId().remove(id);
            return true;
        }
        return false;
    }

}