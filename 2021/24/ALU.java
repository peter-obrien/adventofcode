import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

public class ALU {

    private final List<Instruction> instructions;
    private Queue<Integer> inputs;
    private Map<String, Integer> vars = new HashMap<>();
    // private static Map<Object[],Integer> memo = new HashMap<>();

    public ALU(List<Instruction> ins) {
        this.instructions = ins;
    }

    public int execute(Queue<Integer> inputs) {
        this.inputs = inputs;
        for (Instruction i : instructions) {
            this.processInstruction(i);
        }
        return vars.get("z");
    }

    private Integer getValueSafely(String value) {
        if (value.matches("[w-z]")) {
            return this.vars.getOrDefault(value, 0);
        } else {
            return Integer.parseInt(value);
        }
    }

    public void processInstruction(Instruction ins) {
        System.out.println(ins);
        switch (ins.operation) {
            case "inp":
                vars.put(ins.args[0], inputs.poll());
                break;
            case "add":
                vars.put(ins.args[0], vars.getOrDefault(ins.args[0], 0) + getValueSafely(ins.args[1]));
                break;
            case "mul":
                vars.put(ins.args[0], vars.getOrDefault(ins.args[0], 0) * getValueSafely(ins.args[1]));
                break;
            case "div":
                vars.put(ins.args[0], vars.getOrDefault(ins.args[0], 0) / getValueSafely(ins.args[1]));
                break;
            case "mod":
                vars.put(ins.args[0], vars.getOrDefault(ins.args[0], 0) % getValueSafely(ins.args[1]));
                break;
            case "eql":
                vars.put(ins.args[0], vars.getOrDefault(ins.args[0], 0) == getValueSafely(ins.args[1]) ? 1 : 0);
                break;
            default:
                throw new RuntimeException("Unknown instruction operation: " + ins.operation);
        }
    }

    private static class Instruction {
        final String operation;
        final String[] args;

        public Instruction(String operation, String[] args) {
            this.operation = operation;
            this.args = args;
        }

        public String toString() {
            return operation + " " + args[0] + (args.length > 1 ? " " + args[1] : "");
        }
    }

    public static int dfsBruteForce(ALU alu, int[] value, int depth) {
        
        if (depth == 14) {
            return alu.execute(new LinkedList<Integer>(Arrays.asList(value[0], value[1], value[2], value[3],value[4], value[5],value[6], value[7],value[8], value[9],value[10], value[11],value[12], value[13])));
        } else {
            for (int i = 1; i < 10; i++) {
                value = Arrays.copyOf(value, 14);
                value[depth] = i;
                return dfsBruteForce(alu, value, depth+1);
            }
        }
    }

    public static void main(String[] args) {
        List<Instruction> ins = new LinkedList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("./input.txt"))) {
            while (br.ready()) {
                String line = br.readLine();
                String[] tokens = line.split("\\s");
                ins.add(new Instruction(tokens[0], Arrays.copyOfRange(tokens, 1, tokens.length)));
                // System.out.println(ins.get(ins.size() - 1));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        ALU alu = new ALU(ins);
        dfsBruteForce(alu, "", 1);

    }
}