public class Instruction {
    final String operation;
    final String[] args;

    public Instruction(String operation, String ... args) {
        this.operation = operation;
        this.args = args;
    }
}