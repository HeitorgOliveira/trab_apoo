public enum TipoTarefa {
    ATIVIDADE("atividade"),
    TRABALHO("trabalho"),
    PROVA("prova");
    
    private final String valor;
    
    TipoTarefa(String valor) {
        this.valor = valor;
    }
    
    public String getValor() {
        return valor;
    }
}
