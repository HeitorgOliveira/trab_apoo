public enum TipoAtividade {
    ATIVIDADE("atividade"),
    TRABALHO("trabalho"),
    PROVA("prova");
    
    private final String valor;
    
    TipoAtividade(String valor) {
        this.valor = valor;
    }
    
    public String getValor() {
        return valor;
    }
}
