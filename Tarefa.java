public class Tarefa {
    private double nota;    
    private double peso;
    private TipoAtividade tipo;
    private Disciplina disciplina;

    // Getters e setters gerados pelo Copilot
    public double getNota() {
        return nota;
    }

    public void setNota(double nota) {
        this.nota = nota;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public TipoAtividade getTipo() {
        return tipo;
    }

    public void setTipo(TipoAtividade tipo) {
        this.tipo = tipo;
    }

    public Disciplina getDisciplina() {
        return disciplina;
    }

    public void setDisciplina(Disciplina disciplina) {
        this.disciplina = disciplina;
    }

    public Tarefa(double nota, double peso, TipoAtividade tipo){
        this.nota = nota;
        this.peso = peso;
        this.tipo = tipo;
    }

    \

}