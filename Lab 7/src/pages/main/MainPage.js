import {PizzaCardComponent} from "../../components/pizza-card/PizzaCardComponent.js";
import {PizzaPage} from "../pizza/PizzaPage.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class MainPage {
    constructor(parent) {
        this.parent = parent;
    }

    async getData(){
        return ajax.get(urls.pizzas());
    }

    get page() {
        return document.getElementById('main-page');
    }

    getHTML() {
        return (`<div id="main-page" class="d-flex flex-wrap"><div/>`);
    }

    clickCard(e) {
        const cardId = e.target.dataset.id;

        const pizzaPage = new PizzaPage(this.parent, cardId);
        pizzaPage.render();
    }

    async render(){
        this.parent.innerHTML = '';
        const html = this.getHTML();
        this.parent.insertAdjacentHTML('beforeend', html);

        const data = await this.getData();
        data.data.forEach((item) => {
            const pizzaCard = new PizzaCardComponent(this.page);
            pizzaCard.render(item, this.clickCard.bind(this));
        });
    }
}
