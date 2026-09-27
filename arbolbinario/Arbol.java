package arbolbinario;

public class Arbol {
    private Nodo raiz;

    public Arbol() {
        this.raiz = null;
    }

    public boolean vacio() {
        return this.raiz == null;
    }

    public Nodo buscarNodo(String nombre) {
        if (vacio()) {
            return null;
        }
        return buscarRecursivo(this.raiz, nombre);
    }

    private Nodo buscarRecursivo(Nodo nodoActual, String nombre) {
        if (nodoActual == null) {
            return null;
        }

        int comparacion = nombre.compareTo(nodoActual.nombre);

        if (comparacion == 0) {
            return nodoActual;
        } else if (comparacion < 0) {
        return buscarRecursivo(nodoActual.izquierdo, nombre);
        } else {
            return buscarRecursivo(nodoActual.derecho, nombre);
        }
    }
}
