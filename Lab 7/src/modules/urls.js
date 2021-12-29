class Urls {
    constructor() {
        this.url = 'http://localhost:8000/';
    }

    pizzas() {
        return `${this.url}pizza/`;
    }

    pizza(id) {
        return `${this.url}pizza/${id}/`;
    }
}

export const urls = new Urls();
